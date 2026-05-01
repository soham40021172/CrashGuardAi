# categorical_cleaning.py

import pandas as pd
from loguru import logger


# --------------------------------------------------
# 01 Agency Name Cleaning
# --------------------------------------------------
def clean_agency(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning agency_name...")

    agency_mapping = {
        'MONTGOMERY': 'MONTGOMERY COUNTY POLICE',
        'ROCKVILLE': 'ROCKVILLE POLICE',
        'ROCKVILLE POLICE DEPARTME': 'ROCKVILLE POLICE',
        'GAITHERSBURG': 'GAITHERSBURG POLICE',
        'GAITHERSBURG POLICE DEPAR': 'GAITHERSBURG POLICE',
        'TAKOMA': 'TAKOMA PARK POLICE',
        'TAKOMA PARK POLICE DEPART': 'TAKOMA PARK POLICE',
        'MCPARK': 'MARYLAND-NATIONAL CAPITAL',
        'NAN': 'UNKNOWN'
    }

    df["agency_name_clean"] = (
        df["agency_name"]
        .replace(agency_mapping)
        .fillna("UNKNOWN")
    )

    return df


# --------------------------------------------------
# 02 Route Type Mapping
# --------------------------------------------------
def clean_route_type(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning route_type...")

    route_mapping = {
        'MARYLAND (STATE) ROUTE': 'HIGHWAY',
        'MARYLAND (STATE)': 'HIGHWAY',
        'INTERSTATE (STATE)': 'HIGHWAY',
        'US (STATE)': 'HIGHWAY',
        'RAMP': 'HIGHWAY',
        'SPUR': 'HIGHWAY',

        'COUNTY ROUTE': 'LOCAL',
        'COUNTY': 'LOCAL',
        'MUNICIPALITY ROUTE': 'LOCAL',
        'MUNICIPALITY': 'LOCAL',
        'LOCAL ROUTE': 'LOCAL',
        'SERVICE ROAD': 'LOCAL',
        'CROSSOVER': 'LOCAL',

        'GOVERNMENT ROUTE': 'SPECIAL',
        'PRIVATE ROUTE': 'SPECIAL',
        'BICYCLE ROUTE': 'SPECIAL',
    }

    df["route_type"] = df["route_type"].fillna("UNKNOWN")
    df["route_type_clean"] = df["route_type"].map(route_mapping).fillna("OTHER")

    return df

# --------------------------------------------------
# 03 Collision Type 
# --------------------------------------------------
def clean_collision(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning collision_type...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "REAR" in x:
            return "REAR_END"
        elif "HEAD" in x:
            return "HEAD_ON"
        elif "ANGLE" in x:
            return "ANGLE"
        elif "SIDESWIPE" in x:
            return "SIDESWIPE"
        elif "SINGLE" in x:
            return "SINGLE_VEHICLE"
        else:
            return "OTHER"

    df["collision_type_clean"] = df["collision_type"].apply(categorize)

    return df
# --------------------------------------------------
# 04 Weather
# --------------------------------------------------
def clean_weather(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning weather...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "CLEAR" in x:
            return "CLEAR"
        elif "CLOUD" in x:
            return "CLOUDY"
        elif "RAIN" in x:
            return "RAIN"
        elif "SNOW" in x or "ICE" in x:
            return "WINTER"
        elif "FOG" in x:
            return "FOG"
        else:
            return "OTHER"

    df["weather_clean"] = df["weather"].apply(categorize)

    return df
# --------------------------------------------------
# 05 Surface Condition
# --------------------------------------------------
def clean_surface(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning surface_condition...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "DRY" in x:
            return "DRY"
        elif "WET" in x:
            return "WET"
        elif "SNOW" in x or "ICE" in x:
            return "WINTER"
        else:
            return "OTHER"

    df["surface_condition_clean"] = df["surface_condition"].apply(categorize)

    return df
# --------------------------------------------------
# 06 Light Condition
# --------------------------------------------------
def clean_light(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning light...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "DAYLIGHT" in x:
            return "DAY"
        elif "DARK" in x:
            return "DARK"
        elif "DAWN" in x or "DUSK" in x:
            return "TWILIGHT"
        else:
            return "OTHER"

    df["light_clean"] = df["light"].apply(categorize)

    return df
# --------------------------------------------------
# 07 Traffic Control
# --------------------------------------------------
def clean_traffic(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning traffic_control...")

    def categorize(x):
        if pd.isna(x):
            return "NO_CONTROL"

        x = x.upper()

        if "NO CONTROL" in x:
            return "NO_CONTROL"
        elif "SIGNAL" in x:
            return "TRAFFIC_SIGNAL"
        elif "STOP" in x:
            return "STOP_SIGN"
        else:
            return "OTHER"

    df["traffic_control_clean"] = df["traffic_control"].apply(categorize)

    return df
# --------------------------------------------------
# 08 Driver Substance Abuse
# --------------------------------------------------
def clean_driver_substance(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning driver_substance_abuse...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "NONE" in x:
            return "NONE"
        elif "ALCOHOL" in x:
            return "ALCOHOL"
        elif "DRUG" in x:
            return "DRUG"
        elif "MEDICATION" in x:
            return "MEDICATION"
        elif "COMBIN" in x:
            return "COMBINED"
        else:
            return "OTHER"

    df["driver_substance_abuse_clean"] = df["driver_substance_abuse"].apply(categorize)

    return df
# --------------------------------------------------
# 09 Non Motarist Substance Abuse
# --------------------------------------------------
def clean_non_motorist_substance(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning non_motorist_substance_abuse...")

    def categorize(x):
        if pd.isna(x):
            return "NOT_APPLICABLE"

        x = x.upper()

        if "NONE" in x:
            return "NONE"
        elif "ALCOHOL" in x:
            return "ALCOHOL"
        elif "DRUG" in x:
            return "DRUG"
        elif "MEDICATION" in x:
            return "MEDICATION"
        elif "COMBIN" in x:
            return "COMBINED"
        else:
            return "OTHER"

    df["non_motorist_substance_abuse_clean"] = df["non_motorist_substance_abuse"].apply(categorize)

    return df
# --------------------------------------------------
# 10 Driver Distraction
# --------------------------------------------------
def clean_driver_distraction(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning driver_distracted_by...")

    def categorize(x):
        if pd.isna(x) or x == "UNKNOWN":
            return "UNKNOWN"

        x = x.upper()

        if "NOT DISTRACTED" in x:
            return "NO_DISTRACTION"
        elif "PHONE" in x or "TEXT" in x:
            return "PHONE_RELATED"
        elif "DEVICE" in x:
            return "DEVICE_RELATED"
        elif "OCCUPANT" in x:
            return "IN_VEHICLE"
        else:
            return "OTHER"

    df["driver_distracted_by_clean"] = df["driver_distracted_by"].apply(categorize)

    return df
# --------------------------------------------------
# 11 Driver Liscense State
# --------------------------------------------------
def clean_license_state(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning drivers_license_state...")

    us_states = {
        'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
        'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
        'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT',
        'VA','WA','WV','WI','WY','DC'
    }

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if x == "MD":
            return "IN_STATE"
        elif x in us_states:
            return "OUT_OF_STATE"
        else:
            return "INTERNATIONAL"

    df["drivers_license_state_clean"] = df["drivers_license_state"].apply(categorize)

    return df
# --------------------------------------------------
# 12 Vehicle Damage Extent
# --------------------------------------------------
def clean_vehicle_damage(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning vehicle_damage_extent...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "DESTROYED" in x or "DISABLING" in x:
            return "SEVERE"
        elif "FUNCTIONAL" in x:
            return "MODERATE"
        elif "SUPERFICIAL" in x:
            return "MINOR"
        elif "NO DAMAGE" in x:
            return "NONE"
        else:
            return "UNKNOWN"

    df["vehicle_damage_extent_clean"] = df["vehicle_damage_extent"].apply(categorize)

    return df
# --------------------------------------------------
# 13 Vehicle Impact Location
# --------------------------------------------------
def clean_impact_location(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning vehicle_first_impact_location...")

    front = ['TWELVE OCLOCK','ELEVEN OCLOCK','TEN OCLOCK','ONE OCLOCK','TWO OCLOCK']
    rear = ['SIX OCLOCK','FIVE OCLOCK','SEVEN OCLOCK']
    side = ['THREE OCLOCK','NINE OCLOCK']

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if x in front:
            return "FRONT"
        elif x in rear:
            return "REAR"
        elif x in side:
            return "SIDE"
        else:
            return "OTHER"

    df["vehicle_first_impact_location_clean"] = df["vehicle_first_impact_location"].apply(categorize)

    return df
# --------------------------------------------------
# 14 Vehicle Body Type
# --------------------------------------------------
def clean_vehicle_body_type(df):
    logger.info("Cleaning vehicle_body_type...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "MOTORCYCLE" in x:
            return "TWO_WHEELER"
        elif "BUS" in x:
            return "BUS"
        elif "TRUCK" in x:
            return "HEAVY_TRUCK"
        elif "PICKUP" in x or "VAN" in x:
            return "LIGHT_TRUCK"
        elif "POLICE" in x or "AMBULANCE" in x:
            return "EMERGENCY"
        elif "CAR" in x:
            return "PASSENGER"
        else:
            return "OTHER"

    df["vehicle_body_type_clean"] = df["vehicle_body_type"].apply(categorize)
    return df
# --------------------------------------------------
# 15 Vehicle Movement
# --------------------------------------------------
def clean_vehicle_movement(df):
    logger.info("Cleaning vehicle_movement...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "TURN" in x:
            return "TURNING"
        elif "STOP" in x:
            return "STOPPED"
        elif "LANE" in x:
            return "LANE_CHANGE"
        elif "BACKING" in x or "PARK" in x:
            return "REVERSING"
        elif "MOVING" in x:
            return "MOVING"
        else:
            return "OTHER"

    df["vehicle_movement_clean"] = df["vehicle_movement"].apply(categorize)
    return df
# --------------------------------------------------
# 16 Vehicle Direction
# --------------------------------------------------
def clean_vehicle_direction(df):
    logger.info("Cleaning vehicle_going_dir...")

    def categorize(x):
        if pd.isna(x):
            return "UNKNOWN"

        x = x.upper()

        if "NORTH" in x:
            return "NORTH"
        elif "SOUTH" in x:
            return "SOUTH"
        elif "EAST" in x:
            return "EAST"
        elif "WEST" in x:
            return "WEST"
        else:
            return "UNKNOWN"

    df["vehicle_going_dir_clean"] = df["vehicle_going_dir"].apply(categorize)
    return df
# --------------------------------------------------
# 17 Muncipalty
# --------------------------------------------------
def clean_municipality(df):
    logger.info("Cleaning municipality...")

    df["municipality_clean"] = (
    df["municipality"]
    .replace(["NONE", "None", "none", "", "NAN"], pd.NA)
    .fillna("UNINCORPORATED")
)


    return df
# --------------------------------------------------
# 18 Parked Vehicle
# --------------------------------------------------
def clean_parked_vehicle(df):
    logger.info("Cleaning parked_vehicle...")

    df["parked_vehicle_clean"] = df["parked_vehicle"].fillna("NO")
    df["parked_vehicle_clean"] = df["parked_vehicle_clean"].replace("NAN", "NO")

    return df
# --------------------------------------------------
# 19 Related Non Motarist
# --------------------------------------------------
def clean_related_non_motorist(df):
    logger.info("Cleaning related_non_motorist...")

    def categorize(x):
        if pd.isna(x):
            return "NONE"

        x = x.upper()

        if "PEDESTRIAN" in x:
            return "PEDESTRIAN"
        elif "BICYCL" in x:
            return "BICYCLIST"
        elif "SCOOTER" in x:
            return "SCOOTER"
        else:
            return "OTHER"

    df["related_non_motorist_clean"] = df["related_non_motorist"].apply(categorize)
    return df
# --------------------------------------------------
# 20 Off Road Description
# --------------------------------------------------
def clean_offroad_description(df):
    logger.info("Cleaning off_road_description...")

    df["crash_location_type"] = df["off_road_description"].apply(
        lambda x: "ON_ROAD" if pd.isna(x) else "OFF_ROAD"
    )

    def classify(text):
        if pd.isna(text):
            return "UNKNOWN"

        text = text.upper()

        if "PARKING GARAGE" in text:
            return "PARKING_GARAGE"
        elif "PARKING LOT" in text or "PKG LOT" in text:
            return "PARKING_LOT"
        elif "DRIVEWAY" in text or "DRIVE THRU" in text:
            return "DRIVEWAY"
        elif "ALLEY" in text:
            return "ALLEY"
        elif "SHOULDER" in text:
            return "SHOULDER"
        elif "TRAIL" in text or "PATH" in text:
            return "TRAIL"
        elif "BUS" in text:
            return "BUS_AREA"
        elif "SCHOOL" in text:
            return "SCHOOL_AREA"
        elif "GARAGE" in text:
            return "GARAGE"
        else:
            return "OTHER"

    df["off_road_description_clean"] = df["off_road_description"].apply(classify)

    df["off_road_description"] = df["off_road_description"].fillna("UNKNOWN")
    df["off_road_description"] = df["off_road_description"].replace("NAN", "UNKNOWN")

    return df
# --------------------------------------------------
# 20 Road Catogery + Cross Road Catogery
# --------------------------------------------------
def clean_road_categories(df):
    logger.info("Cleaning road_name & cross_street_name...")

    def derive_category(name):
        if pd.isna(name):
            return "UNKNOWN"

        name = name.upper()

        if "RAMP" in name:
            return "RAMP"

        if any(k in name for k in ["HWY", "FWY", "EXPY", "PKWY", "PIKE"]):
            return "HIGH_SPEED"

        if any(k in name for k in ["BLVD", "AVE"]):
            return "ARTERIAL"

        if any(k in name for k in ["CT", "CIR", "TER", "PL", "LN", "LOOP", "TRL"]):
            return "RESIDENTIAL"

        return "LOCAL"

    df["road_category_clean"] = df["road_name"].apply(derive_category)
    df["cross_road_category_clean"] = df["cross_street_name"].apply(derive_category)

    df["road_name"] = df["road_name"].fillna("UNKNOWN")
    df["road_name"] = df["road_name"].replace("NAN", "UNKNOWN")

    df["cross_street_name"] = df["cross_street_name"].fillna("UNKNOWN")
    df["cross_street_name"] = df["cross_street_name"].replace("NAN", "UNKNOWN")

    return df

def clean_categorical_columns(df):
    logger.info("Starting categorical features cleaning pipeline...")

    df = clean_agency(df)
    df = clean_route_type(df)
    df = clean_municipality(df)
    df = clean_collision(df)
    df = clean_weather(df)
    df = clean_surface(df)
    df = clean_light(df)
    df = clean_traffic(df)
    df = clean_driver_substance(df)
    df = clean_non_motorist_substance(df)
    df = clean_driver_distraction(df)
    df = clean_license_state(df)
    df = clean_vehicle_damage(df)
    df = clean_impact_location(df)
    df = clean_vehicle_body_type(df)
    df = clean_vehicle_movement(df)
    df = clean_vehicle_direction(df)
    df = clean_related_non_motorist(df)
    df = clean_parked_vehicle(df)
    df = clean_offroad_description(df)
    df = clean_road_categories(df)

    logger.info("Categorical features cleaning pipeline completed!")

    return df