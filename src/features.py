import pandas as pd
from utils.haversine_dis import haversine_distance

def create_price_per_sqft(df): # creating a new column for price per square foot
    df["price_per_sqft"] = df["price"] / df["sqft"]
    df["price_per_sqft"] = df["price_per_sqft"].round(2) # round to 2 decimal places
    return df

def ranking_price_per_sqft_system(df):
    bed_ranking = df.groupby("bedrooms")["price_per_sqft"].mean().sort_values(ascending=False).reset_index()
    bed_ranking["bedrooms_rank"] = bed_ranking["price_per_sqft"].rank(ascending=False)
    return df

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

def create_distance_to_poi(df, poi_list, poi_name):
    df[f"distance_to_{poi_name}"] = df.apply(lambda row: nearest_distance(row["latitude"], row["longitude"], poi_list), axis=1)
    return df

