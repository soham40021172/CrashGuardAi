#numerical cleaning.py

import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.cluster import KMeans
from loguru import logger

# ---------------------------------------------------
# Location
# ---------------------------------------------------
def create_location_clusters(df, n_clusters=20):
    logger.info("Creating location clusters...")

    coords = df[["latitude", "longitude"]].dropna()

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    df.loc[coords.index, "location_cluster_clean"] = kmeans.fit_predict(coords)

    return df
# ---------------------------------------------------
# Vehicle Year + Age Engineering
# ---------------------------------------------------
def clean_vehicle_year_features(df):
    logger.info("Cleaning vehicle year + age features...")

    current_year = datetime.now().year

    def clean_year(year):
        if 1950 <= year <= current_year:
            return year
        if year == 0:
            return np.nan
        else:
            return np.nan

    df["vehicle_year_clean"] = df["vehicle_year"].apply(clean_year)

    df["vehicle_age"] = current_year - df["vehicle_year_clean"]

    # Fill missing age by body type median
    global_median = df["vehicle_age"].median()

    df["vehicle_age"] = df.groupby("vehicle_body_type_clean")["vehicle_age"] \
    .transform(lambda x: x.fillna(x.median()) if x.notna().any() else x.fillna(global_median))

    df["vehicle_year_clean"] = df["vehicle_year_clean"].fillna(current_year - df["vehicle_age"])

    return df
# ---------------------------------------------------
# Speed Limit
# ---------------------------------------------------
def clean_speed_limit(df):
    logger.info("Cleaning speed limit...")

    df["speed_limit"] = df["speed_limit"].replace(0, np.nan)
    df["speed_limit"] = df["speed_limit"].fillna(df["speed_limit"].median())

    return df
# ---------------------------------------------------
# Date Time
# ---------------------------------------------------
def create_datetime_features(df):
    logger.info("Creating datetime features...")

    df["crash_date_time"] = pd.to_datetime(
        df["crash_date_time"],
        format="%m/%d/%Y %I:%M:%S %p"
    )

    df["crash_hour"] = df["crash_date_time"].dt.hour
    df["crash_dayofweek"] = df["crash_date_time"].dt.dayofweek
    df["is_weekend"] = df["crash_dayofweek"].isin([5, 6]).astype(int)
    df["crash_month"] = df["crash_date_time"].dt.month

    # Time of day
    bins = [-1, 6, 10, 16, 20, 24]
    labels = ["Late Night", "Morning Rush", "Mid-Day", "Evening Rush", "Night"]

    df["time_of_day_clean"] = pd.cut(df["crash_hour"], bins=bins, labels=labels)

    # Day mapping
    day_mapping = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday",
        3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"
    }

    df["crash_dayofweek_clean"] = df["crash_dayofweek"].map(day_mapping)

    # Month mapping
    month_mapping = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    df["crash_month_clean"] = df["crash_month"].map(month_mapping)

    # Season
    season_map = {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Fall", 10: "Fall", 11: "Fall"
    }

    df["crash_season_clean"] = df["crash_month"].map(season_map)

    df.drop(columns=["crash_date_time"], inplace=True)

    return df

def clean_numerical_columns(df):
    logger.info("Starting numerical features cleaning pipeline...")
    
    df=create_location_clusters(df)
    df=clean_vehicle_year_features(df)
    df=clean_speed_limit(df)
    df=create_datetime_features(df)
    
    logger.info("Numerical features cleaning pipeline completed!")

    return df