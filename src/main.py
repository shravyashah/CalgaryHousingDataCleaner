import pandas as pd
from src.clean import clean_price,clean_address, normalize_address, normalize_garage, clean_garage, clean_days_on_market
from src.features import create_price_per_sqft
from src.rank import score_houses
from src.geocoding import add_geocodes
from src.poi.get_poi import fetch_schools, fetch_grocery_stores

#def check(df, step):
    #print(step, type(df))
#only used for debugging purposes to check the type of the dataframe at each step of the data processing pipeline. It can be uncommented and used as needed to ensure that the dataframe is being processed correctly at each stage.
def main():
    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    df = clean_price(df)
    df = clean_garage(df)
    df = clean_days_on_market(df)

    df = normalize_garage(df)
    df = clean_address(df)
    df = normalize_address(df)

    keep_cols = ["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market"]
    df = df[keep_cols]

    df = add_geocodes(df).round({"latitude": 2, "longitude": 2}) # round to 2 decimal places for better readability and to reduce file size
    df = df[df["geo_valid"]].copy() # keep only rows with valid geocodes for better analysis and visualization
    df = create_price_per_sqft(df) # useful for knowing the price per square foot of the house
    df = score_houses(df)

    #testing poi fetching functions
    print("Fetching schools...")
    schools = fetch_schools()
    print(f"Number of schools found: {len(schools)}")
    print("Fetching grocery stores...")
    grocery_stores = fetch_grocery_stores()
    print(f"Number of grocery stores found: {len(grocery_stores)}")
    
    df.to_csv("data/processed/calgary_houses_processed.csv", index=False)
   
    print(df[["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market", "price_per_sqft","score","latitude","longitude"]].head(54))
    print(df.info())
    
if __name__ == "__main__":
    main()
