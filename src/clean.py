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
    df["price"] = df["price"].fillna(0).astype(int)
    return df

def normalize_garage(df): # normalizing the garage column
    df["garage"] = df["garage"].astype(str).str.lower() # convert to lowercase
    no_value = ["none", "no garage", "n/a", "na", "nan", "null", ""]
    df["garage"] = df["garage"].apply(lambda x: "No" if x in no_value else "Yes") # replace no value with "no garage"
    return df


def clean_garage(df):
    df["garage"] = df["garage"].astype(str)
    return df
