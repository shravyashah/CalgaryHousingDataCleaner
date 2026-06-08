import pandas as pd
import re

def normalize_address(df): # normalizing the address column
    
    abbreviations = { "Northeast": "NE", "Northwest": "NW", "Southeast": "SE", "Southwest": "SW", "Street": "St", "Avenue": "Ave", "Boulevard": "Blvd", "Drive": "Dr", "Road": "Rd", "Lane": "Ln", "Court": "Ct" , "Grv":"Grove",
                     "Circle": "Cir","Circ": "Cir", "Place": "Pl", "Terrace": "Ter","Trail": "Trl", "Parkway": "Pkwy", "Highway": "Hwy", "Close": "Cl", "Crescent": "Cres","Landing": "Lndg", "Way": "Way", "Square": "Sq", "Loop": "Loop", "Point": "Pt", "View": "Vw"}
    for key, value in abbreviations.items():
        df["address"] = df["address"].str.replace(rf"\b{key}\b", value, regex=True,flags=re.IGNORECASE)  # replace full words with abbreviations using regex
    df["address"] = df["address"].str.replace(r"\s+", " ", regex=True).str.strip()
    return df
# This function takes in the dataframe and normalizes the address column by replacing street types and directional indicators with their common abbreviations. 
# It uses a dictionary of abbreviations and iterates through the dictionary to replace the full words with their corresponding abbreviations in the address column of the dataframe. 
# the loop applies to the entire address column but abber is looped to replace the key with the value in the address column. 
# The regex ensures that only whole words are replaced, preventing partial matches from being altered.

def clean_address(df): # cleaning the address column
    df["address"] = df["address"].astype(str)

    df["address"] = df["address"].str.replace(r"#\s*\d+\s*", "", regex=True) # replace "# followed by a number with an empty string to remove unit numbers from the address
    df["address"]= df["address"].str.replace(r"unit\s*\d+\s*", " ", regex=True) # replace "unit" followed by a number with a single space
    df["address"] = df["address"].str.replace(r"\s*-\s*", " ", regex=True)
   
    df = df.dropna(subset=["address"]) # drop rows with missing address values
    df["address"] = df["address"].str.replace(r"\s+", " ", regex=True).str.strip()
    df = df.drop_duplicates(subset=["address"])

    return df
# This function takes in a dataframe and cleans up the address column. It first converts everything into a string and removes any trailing
# white spaces. Then apartments are dealt with by removing unit numbers and the word unit. After addresses are dropped if they do not
# have a value or are a duplicate. Finally Calgary, AB is added to all the values in the column for better geocoding results.

def clean_price(df): # cleaning the price column
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("$", "",regex=False)
    df["price"] = df["price"].str.replace(",", "",regex=False)
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["price"] = df["price"].fillna(0).astype(int)

    df["address"] = df["address"] + ", Calgary, AB"

    return df
# This function converts the values in the col into a string then replaces any symbols such as the dollar sign and the comma
#into a empty string. Then the price is converted to an int and any empty values are filled with 0.

def normalize_garage(df): # normalizing the garage column
    df["garage"] = df["garage"].astype(str).str.lower() # convert to lowercase
    no_value = ["none", "no garage", "n/a", "na", "nan", "null", ""]
    df["garage"] = df["garage"].apply(lambda x: "No" if x in no_value else "Yes") # replace no value with "no garage"
    
    return df
# This function first converts the values in the garage column into lowercases, then a list is made for possible values that indicate
# that there is no function. Then a lambda function is used where "No" is replaced if x is in no_value, otherwise "Yes"

def clean_garage(df): # converting the garage column to "Yes" or "No"
    df["garage"] = df["garage"].astype(str)
    return df
# Ensures all values are a string

def clean_days_on_market(df):
    df["days_on_market"] = pd.to_numeric(df["days_on_market"], errors='coerce')
    df["days_on_market"] = df["days_on_market"].fillna(0).astype(int)
    return df
# Ensures all values are a numeric value and fills any empty values with 0(assuming it is a new listing)