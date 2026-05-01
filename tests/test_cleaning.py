import pandas as pd

from crash_report.pipeline.cleaning.load import run_cleaning_pipeline
from crash_report.db.connection import engine


def test_cleaning_pipeline_runs():
    """
    Test that pipeline runs and creates clean table
    """

    run_cleaning_pipeline()

    df = pd.read_sql("SELECT * FROM crash_reports_analysis_clean LIMIT 5", engine)
    assert df.shape[0] > 0


def test_clean_columns_exist():
    """
    Test that important clean columns are created
    """

    df = pd.read_sql("SELECT * FROM crash_reports_analysis_clean LIMIT 1", engine)

    expected_cols = [
        "agency_name_clean",
        "route_type_clean",
        "location_cluster_clean",
        "vehicle_age",
        "time_of_day_clean"
    ]

    for col in expected_cols:
        assert col in df.columns