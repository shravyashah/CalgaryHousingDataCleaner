import pandas as pd
from clean import clean_price,clean_address, normalize_address, normalize_garage, clean_garage, clean_days_on_market
from features import create_price_per_sqft
from rank import score_houses
from geocoding import add_geocodes


def main():

    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    df = clean_price(df)
    df = clean_garage(df)
    df = normalize_garage(df)
    df = normalize_address(df)
    df = clean_address(df)
    
    df = clean_days_on_market(df)

    keep_cols = ["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market"]
    df = df[keep_cols]

    df = create_price_per_sqft(df) # useful for knowing the price per square foot of the house
    df = score_houses(df)
    df = add_geocodes(df)
    print(df[["address","bedrooms","bathrooms","price","sqft", "garage","community","property_type","days_on_market", "price_per_sqft","score","latitude","longitude"]].head(54))
    print(df.info())
    
    
    

if __name__ == "__main__":
    main()
