import pandas as pd
from utils.haversine_dis import haversine_distance

def create_price_per_sqft(df): # creating a new column for price per square foot
    df["price_per_sqft"] = df["price"] / df["sqft"]
    df["price_per_sqft"] = df["price_per_sqft"].round(2) # round to 2 decimal places
    return df
# Thus function computes the price per sqft of each value in the data frame

def nearest_distance(lat, lon, poi_list): 
    if not poi_list:
            return None
    if pd.isna(lat) or pd.isna(lon):
        return None
    min_distance = float("inf")
    for poi_lat, poi_lon in poi_list:
        distance = haversine_distance(lat, lon, poi_lat, poi_lon)
        if distance < min_distance:
            min_distance = distance
    return min_distance
# This functions purpose is to compute the nearest distance between the address and the poi. It first checks to see if the coord
# is in the poi_list or if it has a value. Then the min distance is set to infinity, to help us find the min distance between the 
#house and the poi. Then the haversine_distance is called to compute the distance and to see if the distance computed is less
#than the min distance

def create_distance_to_poi(df, poi_list, poi_name):
    df[f"distance_to_{poi_name}"] = df.apply(lambda row: nearest_distance(row["latitude"], row["longitude"], poi_list), axis=1)
    return df

# This functions passed in the dataframe, the poi_list,and the type of poi to be applied to the dataframe. Essentially
# this creates a new column of the nearest poi for each row by computinmg the nearest distance.
