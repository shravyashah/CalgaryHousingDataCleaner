import pandas as pd

def normalize_address(df): # normalizing the address column
    abbreviations = { "Northeast": "NE", "Northwest": "NW", "Southeast": "SE", "Southwest": "SW", "Street": "St", "Avenue": "Ave", "Boulevard": "Blvd", "Drive": "Dr", "Road": "Rd", "Lane": "Ln", "Court": "Ct" ,
                     "Circle": "Cir","Circ": "Cir", "Place": "Pl", "Terrace": "Ter","Trail": "Trl", "Parkway": "Pkwy", "Highway": "Hwy", "Close": "Cl", "Crescent": "Cres","Landing": "Lndg", "Way": "Way", "Square": "Sq", "Loop": "Loop", "Point": "Pt", "View": "Vw"}
    for key, value in abbreviations.items():
        df["address"] = df["address"].str.replace(rf"\b{key}\b", value, regex=True) # replace full words with abbreviations using regex
    return df

def clean_address(df): # cleaning the address column
    df["address"] = df["address"].astype(str).str.strip()
    df["address"] = df["address"].str.replace("#",'', regex=False) # replace "#" with "Unit " for better geocoding results
    df["address"] = df["address"].str.replace("-", "", regex=False) # ensure there is a space after "Unit" for better geocoding results
    df = df.dropna(subset=["address"]) # drop rows with missing address values
    df = df.drop_duplicates(subset=["address"])

    df["address"] = df["address"] + ", Calgary, AB" # add city and province to the address for better geocoding results
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

def clean_days_on_market(df):
    df["days_on_market"] = pd.to_numeric(df["days_on_market"], errors='coerce')
    df["days_on_market"] = df["days_on_market"].fillna(0).astype(int)
    return df