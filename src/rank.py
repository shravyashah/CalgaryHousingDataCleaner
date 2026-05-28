import pandas as pd

from features import create_price_per_sqft

def normalize(series):
    return (series - series.min()) / (series.max() - series.min()) if series.max() != series.min() else 0

def score_houses(df):
    df = create_price_per_sqft(df)  # Ensure price_per_sqft is calculated before scoring
    df = df.copy()  # Avoid modifying the original DataFrame

    price = 1- normalize(df["price_per_sqft"]) # lower price per sqft is better, so we take 1 - normalized value
    bedrooms = normalize(df["bedrooms"])
    bathrooms = normalize(df["bathrooms"])
    date_listed = 1 - normalize(df["days_on_market"])  # less time on market is better
    garage = df["garage"].map({"Yes": 1, "No": 0})  # Convert "Yes"/"No" to 1/0

    df["score"] = ((price * 0.4) + (bedrooms * 0.2) + (bathrooms * 0.2) + (date_listed * 0.1) + (garage * 0.1))*100
    df["score"] = df["score"].round(2)  # Round the score to 2 decimal places

    return df


