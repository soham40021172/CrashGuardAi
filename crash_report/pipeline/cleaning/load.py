# load.py

import pandas as pd

from crash_report.db.connection import engine

from crash_report.pipeline.extract import DataExtractor

from crash_report.pipeline.cleaning.clean import run_basic_cleaning_pipeline
from crash_report.pipeline.cleaning.categorical_cleaning import clean_categorical_columns
from crash_report.pipeline.cleaning.numerical_cleaning import clean_numerical_columns


# ==============================
# MAIN CLEANING PIPELINE
# ==============================

def run_cleaning_pipeline():
    
    print("🚀 Starting Cleaning Pipeline...")

    # STEP 1 — Extract Data
    extractor = DataExtractor()
    df = extractor.extract_raw_data()
    print("Data extracted:", df.shape)

    # STEP 2 — Basic Cleaning
    df = run_basic_cleaning_pipeline(df)

    # STEP 3 — Categorical Cleaning
    df = clean_categorical_columns(df)

    # STEP 4 — Numerical & Date Cleaning
    df = clean_numerical_columns(df)

    print("Cleaning completed:", df.shape)

    # STEP 5 — Load into New Table
    df.to_sql(
        "crash_reports_analysis_clean",
        engine,
        if_exists="replace",
        index=False
    )

    print("Clean table created successfully!")
    print("Table Name: crash_reports_analysis_clean")


# ==============================
# RUN PIPELINE
# ==============================

if __name__ == "__main__":
    run_cleaning_pipeline()