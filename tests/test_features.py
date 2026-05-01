# tests/test_features.py

import pandas as pd
from loguru import logger
from crash_report.db.connection import engine
from crash_report.pipeline.feature_engineering.feature_selector import FeatureSelector
from crash_report.pipeline.feature_engineering.feature_transformer import FeatureTransformer


def test_feature_selector():

    logger.info("Testing FeatureSelector...")

    df = pd.read_sql(
        "SELECT * FROM crash_reports_analysis_clean LIMIT 1000",
        engine
    )

    selector = FeatureSelector()

    df_selected = selector.fit_transform(df)

    assert df_selected.shape[0] == df.shape[0], \
        "❌ Selector changed number of rows!"

    assert df_selected.shape[1] > 0, \
        "❌ Selector returned empty dataframe!"

    logger.success("✅ FeatureSelector passed")


def test_feature_transformer():

    logger.info("Testing FeatureTransformer...")

    df = pd.read_sql(
        "SELECT * FROM crash_reports_analysis_clean LIMIT 1000",
        engine
    )

    selector = FeatureSelector()
    transformer = FeatureTransformer()

    df_selected = selector.fit_transform(df)
    df_transformed = transformer.fit_transform(df_selected)

    # 1️⃣ Row consistency
    assert df_transformed.shape[0] == df_selected.shape[0], \
        "❌ Transformer changed number of rows!"

    # 2️⃣ No all-null columns
    null_cols = df_transformed.columns[df_transformed.isnull().all()]
    assert len(null_cols) == 0, \
        f"❌ Columns with all nulls: {null_cols}"

    # 3️⃣ Check duplicate columns
    duplicates = df_transformed.columns[df_transformed.columns.duplicated()]
    assert len(duplicates) == 0, \
        f"❌ Duplicate columns found: {duplicates}"

    # 4️⃣ Basic dtype sanity
    for col in df_transformed.columns:
        if df_transformed[col].dtype == "object":
            assert df_transformed[col].nunique() < 1000, \
                f"⚠ High cardinality column detected: {col}"

    logger.success("✅ FeatureTransformer passed")


def run_all_tests():
    test_feature_selector()
    test_feature_transformer()
    logger.success("🎉 All feature tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()