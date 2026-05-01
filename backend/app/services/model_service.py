import joblib
import pandas as pd
import numpy as np
import shap
import re
from pathlib import Path
from loguru import logger

class ModelService:
    def __init__(self):
        self.model_dir = Path(__file__).resolve().parent.parent.parent / "models"
        
        # Load Artifacts
        self.pipeline = joblib.load(self.model_dir / "crash_model.pkl")
        self.threshold = joblib.load(self.model_dir / "threshold.pkl")
        self.schema = joblib.load(self.model_dir / "feature_schema.pkl")
        
        # Breakdown Pipeline for SHAP
        self.model = self.pipeline.named_steps["model"]
        self.preprocessor = self.pipeline.named_steps["preprocessing"]
        
        # Initialize Explainer once (Industrial best practice for speed)
        self.explainer = shap.TreeExplainer(self.model)
        
        self.injury_thresholds = {
            "NO APPARENT INJURY": (0.00, 0.30),
            "POSSIBLE INJURY": (0.31, 0.40),
            "SUSPECTED MINOR INJURY": (0.41, 0.47),
            "SUSPECTED SERIOUS INJURY": (0.48, 0.85),
            "FATAL INJURY": (0.86, 1.00)}

        self.original_feature_list = [
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

    def extract_original_feature(self,name, og_cols):
        clean_name = re.sub(r"^(cat__|num__)", "", name)
        
        for col in sorted(og_cols, key=len, reverse=True):
            if clean_name.startswith(col):
                return col
                
        return clean_name

    def _classify_injury(self, score):
        for label, (low, high) in self.injury_thresholds.items():
            if low <= score <= high:
                return label
        return "Unknown"

    def predict_severity(self, input_data: dict):
        # 1. Prepare and Validate Data
        record = pd.DataFrame([input_data])
        
        # Ensure columns match training schema (categorical + numeric)
        expected_cols = self.schema["categorical"] + self.schema["numeric"]
        record = record[expected_cols] 
        
        # 2. Get Probability
        proba = self.pipeline.predict_proba(record)[0][1]
        prediction = 1 if proba >= self.threshold else 0
        
        # 3. SHAP Explanation Logic
        # Transform data through everything EXCEPT the final model step
        processed_data = self.pipeline[:-1].transform(record)
        if hasattr(processed_data, "toarray"):
            processed_data = processed_data.toarray()
            
        shap_values = self.explainer.shap_values(processed_data)
        
        # Correctly handle SHAP output for Random Forest (index 1 is the 'Positive' class)
        if isinstance(shap_values, list):
            # For some SHAP versions/RF setups
            shap_values_single = shap_values[1][0]
        else:
            # For newer SHAP versions
            shap_values_single = shap_values[0, :, 1] if shap_values.ndim == 3 else shap_values[0]

        feature_names = self.preprocessor.get_feature_names_out()
        shap_df = pd.DataFrame({"feature": feature_names, "shap_value": shap_values_single})
        
        shap_df["original_feature"] = shap_df["feature"].apply(
            lambda x: self.extract_original_feature(x, self.original_feature_list)
        )
        
        agg_shap = shap_df.groupby("original_feature")["shap_value"].sum().reset_index()
        agg_shap["abs_value"] = np.abs(agg_shap["shap_value"])
        top_5 = agg_shap.sort_values("abs_value", ascending=False).head(5)

        # 5. Build Human-Readable JSON
        explanations = []
        for _, row in top_5.iterrows():
            readable_name = row["original_feature"].replace("_clean", "").replace("_", " ").title()
            
            explanations.append({
                "feature": readable_name,
                "impact_score": float(round(row["shap_value"], 5)),
                "effect": "increased" if row["shap_value"] > 0 else "decreased",
                "severity_contribution": "High" if row["abs_value"] > 0.05 else "Moderate"
            })

        return {
            "probability": float(round(proba, 4)),
            "prediction": int(prediction),
            "injury_type": self._classify_injury(proba),
            "top_factors": explanations,
            "safety_score": round((1 - proba) * 100, 1)
        }