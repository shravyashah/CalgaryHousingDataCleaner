
from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="calgary_housing")

def fetch_schools():
    # Placeholder for fetching school data
    # call API from a service like OpenStreetMap or a local database to get nearby schools based on geocoded coordinates
    return ["School A", "School B", "School C"]

def fetch_grocery_stores():
    # Placeholder for fetching grocery store data
    # call API from a service like OpenStreetMap or a local database to get nearby grocery stores based on geocoded coordinates
    return ["Grocery Store A", "Grocery Store B", "Grocery Store C"]

def load_poi_data(df):
    df["nearby_schools"] = df.apply(lambda row: fetch_schools(), axis=1) # fetch nearby schools for each property
    df["nearby_grocery_stores"] = df.apply(lambda row: fetch_grocery_stores(), axis=1) # fetch nearby grocery stores for each property
    return df
def save_poi_data(df):
    # Placeholder for saving POI data
    #df.to_csv("data/processed/calgary_houses_with_poi.csv", index=False) # save the updated DataFrame with POI data to a new CSV file
    pass