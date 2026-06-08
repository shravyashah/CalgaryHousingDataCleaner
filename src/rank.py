import pandas as pd
from src.features import create_price_per_sqft

def normalize(series):
    if series.max() == series.min():
        return pd.Series(0, index=series.index)  # Return a series of zeros if all values are the same to avoid division by zero
    return (series - series.min()) / (series.max() - series.min()) if series.max() != series.min() else 0

def score_houses(df):
    df = create_price_per_sqft(df)  # Ensure price_per_sqft is calculated before scoring
    df = df.copy()  # Avoid modifying the original DataFrame

    price = 1- normalize(df["price_per_sqft"]) # lower price per sqft is better, so we take 1 - normalized value
    bedrooms = normalize(df["bedrooms"])
    bathrooms = normalize(df["bathrooms"])
    date_listed = 1 - normalize(df["days_on_market"])  # less time on market is better
    garage = df["garage"].map({"Yes": 1, "No": 0})  # Convert "Yes"/"No" to 1/0
    school_distance = 1 - normalize(df["distance_to_schools"])  # closer to schools is better
    grocery_distance = 1 - normalize(df["distance_to_grocery_stores"]) 

    df["score"] = ((price * 0.3) + (bedrooms * 0.1) + (bathrooms * 0.1) + (date_listed * 0.1) + (garage * 0.1) + (school_distance * 0.1) + (grocery_distance * 0.2)) * 100
    df["score"] = df["score"].round(2)  # Round the score to 2 decimal places

    return df

