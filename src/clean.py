import pandas as pd

def clean_price(df): # cleaning the price column
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("$", "",regex=False)
    df["price"] = df["price"].str.replace(",", "",regex=False)
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["price"] = df["price"].fillna(0)
    df["price"] = df["price"].astype(int)
    return df

def clean_address(df): # cleaning the address column
    df["address"] = df["address"].drop_duplicates()
    return df