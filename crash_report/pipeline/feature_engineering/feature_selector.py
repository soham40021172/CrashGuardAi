# pipeline/features/feature_selector.py

import logging
from sklearn.base import BaseEstimator, TransformerMixin

logger = logging.getLogger(__name__)


class FeatureSelector(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.uncleaned_cols = ['agency_name',
        'collision_type',
        'crash_dayofweek',
        'crash_month',
        'cross_street_name',
        'driver_distracted_by',
        'driver_substance_abuse',
        'drivers_license_state',
        'light','municipality',
        'non_motorist_substance_abuse',
        'off_road_description',
        'parked_vehicle',
        'related_non_motorist',
        'road_name',
        'route_type',
        'surface_condition',
        'traffic_control',
        'vehicle_body_type',
        'vehicle_damage_extent',
        'vehicle_first_impact_location',
        'vehicle_going_dir',
        'vehicle_movement',
        'vehicle_year',
        'weather']

        self.post_event_cols = ['driver_at_fault',
        'vehicle_damage_extent_clean']

        self.messy_cols = ['acrs_report_type',
        'agency_name_clean',
        'latitude',
        'longitude',]

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        logger.info("Running FeatureSelector...")

        X = X.copy()

        cols_to_drop = (
            self.uncleaned_cols +
            self.post_event_cols +
            self.messy_cols
        )

        existing = [col for col in cols_to_drop if col in X.columns]

        if existing:
            logger.info(f"Dropping {len(existing)} columns.")
            X = X.drop(columns=existing)

        return X