import pandas as pd
from src.poi.get_poi import fetch_schools, fetch_grocery_stores
import os

os.makedirs("data/processed", exist_ok=True) # create the directory if it doesn't exist

print("Loading schools data...")
schools = fetch_schools() # load the latitude and longitude of schools in Calgary
pd.DataFrame(schools, columns=["latitude", "longitude"]).to_csv("data/processed/schools.csv", index=False) # save the schools data to a CSV file for future use

print("Loading grocery stores data...")
grocery_stores = fetch_grocery_stores() # load the latitude and longitude of grocery stores in Calgary
pd.DataFrame(grocery_stores, columns=["latitude", "longitude"]).to_csv("data/processed/grocery_stores.csv", index=False) # save the grocery stores data to a CSV file for future use

print("Data loading complete. Schools and grocery stores data have been saved to the data/processed directory.")