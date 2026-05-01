# modeling/predict.py

import joblib
import pandas as pd
import numpy as np
import shap
import re
from loguru import logger
from crash_report.db.connection import engine
from crash_report.config import MODELS_DIR


def validate_schema(df, schema):

    expected_cols = schema["categorical"] + schema["numeric"]

    missing = set(expected_cols) - set(df.columns)
    extra = set(df.columns) - set(expected_cols)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if extra:
        logger.warning(f"Dropping unexpected columns: {extra}")
        df = df.drop(columns=list(extra))

    df = df[expected_cols]

    return df


def run_predection():
    
    sample_input = {
        "collision_type_clean": "REAR_END",
        "crash_dayofweek_clean": "Friday",
        "crash_location_type": "ON_ROAD",
        "crash_season_clean": "Spring",
        "cross_road_category_clean": "ARTERIAL",
        "driver_distracted_by_clean": "NO_DISTRACTION",
        "drivers_license_state_clean": "IN_STATE_MD",
        "driver_substance_abuse_clean": "NONE",
        "driverless_vehicle": 0,
        "is_incorporated": 1,
        "is_weekend": 0,
        "light_clean": "DAY",
        "location_cluster_clean": 5,
        "non_motorist_substance_abuse_clean": 0,
        "parked_vehicle_clean": 0,
        "related_non_motorist_clean": 0,
        "road_category_clean": "ARTERIAL",
        "route_type_clean": "Highway/Main",
        "speed_limit": 38,
        "surface_condition_clean": "WET",
        "time_of_day_clean": "Evening Rush",
        "traffic_control_clean": "TRAFFIC_SIGNAL",
        "vehicle_age": 5,
        "vehicle_body_type_clean": "PASSENGER_VEHICLE",
        "vehicle_first_impact_location_clean": "FRONT",
        "vehicle_going_dir_clean": "NORTH",
        "vehicle_movement_clean": "STRAIGHT_DRIVING",
        "weather_clean": "RAIN"
    }

    pipeline = joblib.load(MODELS_DIR / "crash_model.pkl")
    threshold = joblib.load(MODELS_DIR / "threshold.pkl")
    schema = joblib.load(MODELS_DIR / "feature_schema.pkl")

    record = pd.DataFrame([sample_input])

    record = validate_schema(record, schema)

    injury_thresholds = {
        "NO APPARENT INJURY": (0.00, 0.30),
        "POSSIBLE INJURY": (0.31, 0.40),
        "SUSPECTED MINOR INJURY": (0.41, 0.47),
        "SUSPECTED SERIOUS INJURY": (0.48, 0.85),
        "FATAL INJURY": (0.86, 1.00)
    }

    proba = pipeline.predict_proba(record)[0][1]
    prediction = 1 if proba >= threshold else 0

    def classify_injury(score):
        for label , (low,high) in injury_thresholds.items():
            if low <= score <=high:
                return label
        return "Unknown"
              
    logger.info(f"Injury Probability: {proba}")
    logger.info(f"Predicted Injury: {prediction}")
    logger.info(f"Injury Type: {classify_injury(proba)}")
    

    #------------------------------------------------------
    #---------------------Shap Logic-----------------------
    #------------------------------------------------------

    selector = pipeline.named_steps["selector"]
    transformer = pipeline.named_steps["transformer"]
    preprocessor = pipeline.named_steps["preprocessing"]
    model = pipeline.named_steps["model"]

    # Feature engineering
    record_fe = selector.transform(record)
    record_fe = transformer.transform(record_fe)

    # Preprocessing
    record_processed = preprocessor.transform(record_fe)

    if hasattr(record_processed, "toarray"):
        record_processed = record_processed.toarray()

    record_processed = record_processed.astype(np.float64)

    feature_names = preprocessor.get_feature_names_out()

    # SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(record_processed)
    shap_values = np.array(shap_values)

    # Handle binary classification output
    if shap_values.ndim == 3:
        shap_values_single = shap_values[0][:, 1]
    elif shap_values.ndim == 2:
        shap_values_single = shap_values[0]
    else:
        raise ValueError(f"Unexpected SHAP shape: {shap_values.shape}")

    # -----------------------------------------
    # Aggregate OHE back to original features
    # -----------------------------------------

    shap_df = pd.DataFrame({
        "feature": feature_names,
        "shap_value": shap_values_single
    })
    
    original_feature_list = [
        "collision_type_clean",       "crash_dayofweek_clean",    "crash_location_type",
        "crash_season_clean",         "cross_road_category_clean", "driver_distracted_by_clean",
        "drivers_license_state_clean", "driver_substance_abuse_clean", "driverless_vehicle",
        "is_incorporated",            "is_weekend",               "light_clean",
        "location_cluster_clean",     "non_motorist_substance_abuse_clean", "parked_vehicle_clean",
        "related_non_motorist_clean", "road_category_clean",      "route_type_clean",
        "speed_limit",                "surface_condition_clean",  "time_of_day_clean",
        "traffic_control_clean",      "vehicle_age",              "vehicle_body_type_clean",
        "vehicle_first_impact_location_clean", "vehicle_going_dir_clean", "vehicle_movement_clean",
        "weather_clean"
    ]

    def extract_original_feature(name, og_cols):
        # Remove pipeline prefixes first
        clean_name = re.sub(r"^(cat__|num__)", "", name)
        
        # Check if the clean_name starts with any of our original column names
        # We sort by length (longest first) so 'vehicle_body_type_clean' 
        # is matched before a shorter partial match.
        for col in sorted(og_cols, key=len, reverse=True):
            if clean_name.startswith(col):
                return col
                
        return clean_name

    shap_df["original_feature"] = shap_df["feature"].apply(
        lambda x: extract_original_feature(x, original_feature_list)
    )

    # Aggregate absolute impact
    agg_shap = (
        shap_df
        .groupby("original_feature")["shap_value"]
        .sum()
        .reset_index()
    )
    
    logger.info(agg_shap)
    agg_shap["abs_value"] = np.abs(agg_shap["shap_value"])
    agg_shap = agg_shap.sort_values("abs_value", ascending=False)

    top_5 = agg_shap.head(5)

    # -----------------------------------------
    # Human readable explanation
    # -----------------------------------------

    explanations = []

    for _, row in top_5.iterrows():
        feature = row["original_feature"]
        impact = row["shap_value"]

        direction = "increased" if impact > 0 else "decreased"

        explanations.append({
            "feature": feature,
            "impact_score": float(round(impact, 5)),
            "effect": direction
        })

    logger.info("Top 5 Factors Influencing This Prediction:")

    for item in explanations:
        logger.info(
            f"{item['feature']} → {item['effect']} injury risk "
            f"(impact={item['impact_score']})"
        )

    # OPTIONAL: return JSON for frontend
    return {
        "probability": float(round(proba, 4)),
        "prediction": int(prediction),
        "injury_type": classify_injury(proba),
        "top_factors": explanations
    }



if __name__ == "__main__":
    run_predection()