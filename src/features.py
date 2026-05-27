import pandas as pd

def create_price_per_sqft(df): # creating a new column for price per square foot
    df["price_per_sqft"] = df["price"] / df["sqft"]
    df["price_per_sqft"] = df["price_per_sqft"].round(2) # round to 2 decimal places
    return df