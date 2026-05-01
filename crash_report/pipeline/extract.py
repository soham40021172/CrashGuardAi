# extract.py

import pandas as pd
from loguru import logger
from crash_report.db.connection import DatabaseConnection


class DataExtractor:

    def __init__(self):
        self.db = DatabaseConnection()
        self.engine = self.db.get_engine()

    def extract_raw_data(self, table_name="crash_reports"):
        """
        Extract raw crash data from PostgreSQL
        """
        try:
            logger.info("Starting data extraction from database...")

            query = f"SELECT * FROM public.{table_name}"
            df = pd.read_sql(query, self.engine)

            logger.success(f"Data extracted successfully. Rows: {len(df)}")

            return df

        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            raise