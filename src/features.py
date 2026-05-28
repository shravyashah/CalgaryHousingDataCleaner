import pandas as pd

def create_price_per_sqft(df): # creating a new column for price per square foot
    df["price_per_sqft"] = df["price"] / df["sqft"]
    df["price_per_sqft"] = df["price_per_sqft"].round(2) # round to 2 decimal places
    return df


def ranking_price_per_sqft_system(df):
    bed_ranking = df.groupby("bedrooms")["price_per_sqft"].mean().sort_values(ascending=False).reset_index()
    bed_ranking["bedrooms_rank"] = bed_ranking["price_per_sqft"].rank(ascending=False)
    return df

