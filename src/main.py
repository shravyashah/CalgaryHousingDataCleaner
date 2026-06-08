# all import statements
import pandas as pd
from src.clean import clean_price,clean_address, normalize_address, normalize_garage, clean_garage, clean_days_on_market
from src.features import create_price_per_sqft
from src.rank import score_houses
from src.geocoding import load_geocodes, is_valid_geocode
from src.poi.get_poi import load_schools, load_grocery_stores
from src.features import create_distance_to_poi

#def check(df, step):
    #print(step, type(df))
#only used for debugging purposes to check the type of the dataframe at each step of the data processing pipeline. It can be uncommented and used as needed to ensure that the dataframe is being processed correctly at each stage.
def main():
    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False) # read the raw data from the CSV file into a pandas dataframe.
   
    # cleaning and preprocessing the data by calling functions in the clean.py module to clean the price, garage, days on market, and address columns, and normalize the garage and address columns. 
    # The cleaned and normalized data is then stored back in the dataframe keep_cols.
    df = clean_price(df)
    df = clean_garage(df)
    df = clean_days_on_market(df)
    df = normalize_garage(df)
    df = clean_address(df)
    df = normalize_address(df)

    print("START:", len(df))

    df1 = clean_address(df)
    print("AFTER CLEAN:", len(df1))

    df2 = normalize_address(df1)
    print("AFTER NORMALIZE:", len(df2))


    keep_cols = ["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market"]
    df = df[keep_cols]

    # loads geocodes from the cache file in a dict format where the key is the address and the value is the tuple of coord.
    # checks to see if the geocodes are valid (not None and not NaN) and filters out any invalid geocodes from the dictionary. 
    # Then, it merges the geocoded latitude and longitude with the original dataframe based on the address column, and drops any rows where geocoding failed and latitude or longitude is missing.
    geo_df = load_geocodes() # load the geocoded latitude and longitude for each address from the cache file and add them to the dataframe
    geo_df = {addr: (lat, lon) for addr, (lat, lon) in geo_df.items() if is_valid_geocode(lat, lon)} # filter out invalid geocodes
    df = df.merge(pd.DataFrame.from_dict(geo_df, orient="index", columns=["latitude", "longitude"]), left_on="address", right_index=True, how="left") # merge the geocoded latitude and longitude with the original dataframe based on the address column
    df = df.dropna(subset=["latitude", "longitude"], how = "all") # drop rows where geocoding failed and latitude or longitude is missing
    
    #where features are implemented and creates new columns to be in the processed dataframe
    #also the score function is called to rank houses based on a score out of 100
    df = create_price_per_sqft(df) # useful for knowing the price per square foot of the house
    df = create_distance_to_poi(df, load_schools(), "schools") # create a new column for the distance to the nearest school
    df = create_distance_to_poi(df, load_grocery_stores(), "grocery_stores") # create a new column for the distance to the nearest grocery store
    df = score_houses(df)

    # current dataframe is saved to a new CSV file where data is cleaned, features are created and houses are scored
    df.to_csv("data/processed/calgary_houses_processed.csv", index=False)
   
    print(df[["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market", "price_per_sqft","distance_to_schools","distance_to_grocery_stores","latitude","longitude","score"]].head(60))
    print(df[["address","score", "distance_to_schools", "distance_to_grocery_stores"]])
    print(df.info())
 # this is where the pipeline is executed when the script is run and then goes in order of the steps in main   
if __name__ == "__main__":
    main()
