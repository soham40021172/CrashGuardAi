# modeling/train.py

import joblib
import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from crash_report.db.connection import engine
from crash_report.config import MODELS_DIR,BACKEND_MODELS_DIR
from crash_report.pipeline.feature_engineering.feature_selector import FeatureSelector
from crash_report.pipeline.feature_engineering.feature_transformer import FeatureTransformer


THRESHOLD = 0.48


def run_train():

    logger.info("Loading cleaned table from database...")

    df = pd.read_sql(
        "SELECT * FROM crash_reports_analysis_clean",
        engine
    )

    logger.info(f"Data shape: {df.shape}")
    df["target"] = df["injury_severity"].apply(
        lambda x: 0 if x == "NO APPARENT INJURY" else 1
    )
    df=df.drop(columns='injury_severity')

    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    # -----------------------------------------
    # Step 1: Run feature engineering once
    # -----------------------------------------
    feature_pipeline = Pipeline([
        ("selector", FeatureSelector()),
        ("transformer", FeatureTransformer()),
    ])

    X_train_transformed = feature_pipeline.fit_transform(X_train)

    categorical_cols = X_train_transformed.select_dtypes(
        include="object"
    ).columns.tolist()

    numeric_cols = X_train_transformed.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    logger.info(f"Categorical columns: {categorical_cols}")
    logger.info(f"Numeric columns: {numeric_cols}")
    logger.info("--- Inspection of Transformed Features ---")

    for col in X_train_transformed.columns:
        logger.info(f"Feature: {col}")
        # Show unique values after FeatureSelector and FeatureTransformer ran
        unique_vals = X_train_transformed[col].unique()
        logger.info(f"Unique Values ({len(unique_vals)}): {unique_vals}")
        logger.info('------------------------------------------')

    # For the target y, it hasn't changed except for the 0/1 mapping
    logger.info(f"Target unique values: {y.unique()}")    
    # Save schema BEFORE encoding
    feature_schema = {
        "categorical": categorical_cols,
        "numeric": numeric_cols
    }
     
    # -----------------------------------------
    # Step 2: Full ML Pipeline
    # -----------------------------------------
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )
    
    model_pipeline = Pipeline([
        ("selector", FeatureSelector()),
        ("transformer", FeatureTransformer()),
        ("preprocessing", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=400,
            max_depth=12,
            min_samples_leaf=10,
            min_samples_split=20,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        ))
    ])

    logger.info("Training model...")
    model_pipeline.fit(X_train, y_train)

    save_dirs = [MODELS_DIR, BACKEND_MODELS_DIR]
        
    for directory in save_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        
        # Save the 3 main artifacts
        joblib.dump(feature_schema, directory / "feature_schema.pkl")
        joblib.dump(model_pipeline, directory / "crash_model.pkl")
        joblib.dump(THRESHOLD, directory / "threshold.pkl")
        
        logger.info(f"Artifacts synced to: {directory}")

    logger.success("Model, schema, and threshold successfully saved to Root and Backend folders.")


if __name__ == "__main__":
    run_train()