import pandas as pd
from clean import clean_price,clean_address, normalize_address, normalize_garage, clean_garage
from features import create_price_per_sqft


def main():

    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    df = clean_price(df)
    df = normalize_garage(df)
    df = clean_garage(df)
    df = normalize_address(df)
    df = clean_address(df)

    keep_cols = ["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_market"]
    df = df[keep_cols]

    df = create_price_per_sqft(df) # useful for knowing the price per square foot of the house
    print(df[["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_market", "price_per_sqft"]].head(54))
    print(df.info())
    
    

if __name__ == "__main__":
    main()
