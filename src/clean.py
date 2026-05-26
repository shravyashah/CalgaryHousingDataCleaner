import pandas as pd

def clean_price(df): # cleaning the price column
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("$", "",regex=False)
    df["price"] = df["price"].str.replace(",", "",regex=False)
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["price"] = df["price"].astype(int)
    return df

def normalize_address(df): # normalizing the price column
    
    return df

def clean_address(df): # cleaning the address column
    df = df.dropna(subset=["address"]) # drop rows with missing address values
    df = df.drop_duplicates(subset=["address"])
    return df