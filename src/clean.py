import pandas as pd

def normalize_address(df): # normalizing the address column
    abbreviations = { "NorthEast": "NE", "NorthWest": "NW", "SouthEast": "SE", "SouthWest": "SW", "Street": "St", "Avenue": "Ave", "Boulevard": "Blvd", "Drive": "Dr", "Road": "Rd", "Lane": "Ln", "Court": "Ct" }
    for key, value in abbreviations.items():
        df["address"] = df["address"].str.replace(rf"\b{key}\b", value, regex=True) # replace full words with abbreviations using regex
    return df

def clean_address(df): # cleaning the address column
    df = df.dropna(subset=["address"]) # drop rows with missing address values
    df = df.drop_duplicates(subset=["address"])
    return df

def clean_price(df): # cleaning the price column
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("$", "",regex=False)
    df["price"] = df["price"].str.replace(",", "",regex=False)
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["price"] = df["price"].astype(int)
    return df

def clean_lotsize(df): # cleaning the lot_size column
    df["lot_size"] = df["lot_size"].astype(str)
    df["lot_size"] = df["lot_size"].str.replace(",", "",regex=False)
    df["lot_size"] = df["lot_size"].str.replace("sqft", "",regex=False)
    df["lot_size"] = pd.to_numeric(df["lot_size"], errors='coerce')
    return df