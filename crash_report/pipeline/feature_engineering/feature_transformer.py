# pipeline/features/feature_transformer.py

import pandas as pd
import numpy as np
import logging
from sklearn.base import BaseEstimator, TransformerMixin

logger = logging.getLogger(__name__)


class FeatureTransformer(BaseEstimator, TransformerMixin):

    def __init__(self):
        """
        No learned parameters yet.
        If in future we need to learn bins or thresholds,
        we can store them inside self during fit().
        """
        pass

    # -------------------------------------------------
    # Fit (nothing to learn currently)
    # -------------------------------------------------
    def fit(self, X, y=None):
        return self

    # -------------------------------------------------
    # Transform
    # -------------------------------------------------
    def transform(self, X):

        logger.info("Running FeatureTransformer...")

        X = X.copy()

        # ---------------------------------------------
        # Category Consolidation
        # ---------------------------------------------
        X = self._consolidate_categories(X)

        # ---------------------------------------------
        # Binary Flags
        # ---------------------------------------------
        X = self._create_binary_flags(X)

        # ---------------------------------------------
        # Drop Additional Columns
        # ---------------------------------------------
        X = self._drop_additional_columns(X)

        # ---------------------------------------------
        # Binning
        # ---------------------------------------------
        X = self._bin_numerical_features(X)

        logger.info("FeatureTransformer completed.")

        return X

    # =================================================
    # Internal Methods
    # =================================================

    def _consolidate_categories(self, df):

        replace_map = {
            "drivers_liscense_test_clean":{"INTERNATIONAL": "OTHER","US_TERRITORY": "OTHER"},
            "collision_type_clean": {"UNKNOWN": "OTHER"},
            "weather_clean": {"WIND": "OTHER", "DUST": "OTHER"},
            "surface_condition_clean": {"LOOSE_SURFACE": "OTHER"},
            "light_clean": {"OTHER": "UNKNOWN"},
            "traffic_control_clean": {
                "FLASHING_SIGNAL": "OTHER",
                "SCHOOL_ZONE": "OTHER",
                "RAILROAD": "OTHER",
            },
            "driver_substance_abuse_clean": {
                        "MEDICATION": "DRUG",
                        "COMBINED": "DRUG",
                        "OTHER": "DRUG",
                    },
            "driver_distracted_by_clean": {
                "DEVICE_RELATED": "DISTRACTION",
                "PHONE_RELATED": "DISTRACTION",
                "IN_VEHICLE_DISTRACTION": "DISTRACTION",
                "OTHER": "DISTRACTION",
            },
            "vehicle_body_type_clean": {
                "INDUSTRIAL_FARM": "OTHER",
                "OFF_ROAD": "OTHER",
            },
            "vehicle_movement_clean": {"DRIVERLESS": "UNKNOWN"},
            "vehicle_going_dir_clean": {"NOT_ON_ROAD": "UNKNOWN"},
        }

        for col, mapping in replace_map.items():
            if col in df.columns:
                df[col] = df[col].replace(mapping)

        if "location_cluster_clean" in df.columns:
           df["location_cluster_clean"] = df["location_cluster_clean"].astype(str) 
        return df

    def _create_binary_flags(self, df):

        if "non_motorist_substance_abuse_clean" in df.columns:
            df["non_motorist_substance_abuse_clean"] = df[
                "non_motorist_substance_abuse_clean"
            ].apply(lambda x: 0 if x in ["NOT_APPLICABLE", "NONE", "UNKNOWN"] else 1)

        if "related_non_motorist_clean" in df.columns:
            df["related_non_motorist_clean"] = df[
                "related_non_motorist_clean"
            ].apply(lambda x: 0 if x == "NONE_OR_UNKNOWN" else 1)
       
        if 'municipality_clean' in df.columns:
            # Create the feature, but DON'T expect it in the raw input schema
            df['is_incorporated'] = df['municipality_clean'].astype(str).str.upper().apply(
                lambda x: 0 if x == "UNINCORPORATED" else 1
            )

        if 'parked_vehicle_clean' in df.columns:
            df['parked_vehicle_clean'] = df[
                'parked_vehicle_clean'
                ].apply(lambda x: 1 if x == "YES" else 0)

        if 'driverless_vehicle' in df.columns:
            df['driverless_vehicle'] = df['driverless_vehicle'].astype(str).str.upper().apply(
                lambda x: 0 if x in ["NO", "0", "FALSE"] else 1
            )

        return df

    def _drop_additional_columns(self, df):

        cols_to_drop = [
            "crash_hour",
            "crash_month_clean",
            "off_road_description_clean",
            "vehicle_year_clean",
            'municipality_clean'
        ]

        existing = [col for col in cols_to_drop if col in df.columns]
        df = df.drop(columns=existing)

        return df

    def _bin_numerical_features(self, df):

        if "vehicle_age" in df.columns:
            df["vehicle_age"] = pd.cut(
                df["vehicle_age"].fillna(-1), 
                bins=[ -1, 10, 20, 30, 40, np.inf],
                labels=['0-10', '10-20', '20-30', '30-40', '40+']
            ).astype(str) # Convert to string for OneHotEncoder

        if "speed_limit" in df.columns:
            df["speed_limit"] = pd.cut(
                df["speed_limit"].fillna(-1),
                bins=[-1, 10, 20, 30, 40, np.inf],
                labels=['0-10', '10-20', '20-30', '30-40', '40+']
            ).astype(str)

        return df