# clean.py

import pandas as pd
from loguru import logger


# --------------------------------------------------
# 01 Remove duplicates
# --------------------------------------------------
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Removing duplicate rows...")
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    logger.success(f"Removed {before - after} duplicate rows")
    return df


# --------------------------------------------------
# 02 Standardize categorical text
# --------------------------------------------------
def standardize_text(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Standardizing categorical text columns...")

    cat_cols = df.select_dtypes(include=["object"]).columns

    for col in cat_cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.upper()
    return df


# --------------------------------------------------
# 03 Drop useless columns
# --------------------------------------------------
def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Dropping unused columns...")

    cols_to_drop = [
        "person_id",
        "vehicle_id",
        "report_number",
        "local_case_number",
        "location",
        "vehicle_make",
        "vehicle_model",
        "circumstance"
    ]

    df = df.drop(columns=cols_to_drop, errors="ignore")
    return df


# --------------------------------------------------
# 04 Filter target column
# --------------------------------------------------
def filter_target_column(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Filtering rows with missing injury_severity...")
    df = df.dropna(subset=["injury_severity"])
    return df


# --------------------------------------------------
# MASTER BASIC CLEANING PIPELINE
# --------------------------------------------------
def run_basic_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("🚀 Running BASIC cleaning pipeline...")

    df = remove_duplicates(df)
    df = standardize_text(df)
    df = drop_unused_columns(df)
    df = filter_target_column(df)

    logger.success("Basic cleaning completed!")

    return df