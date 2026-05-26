import pandas as pd
from clean import clean_price,clean_address, normalize_address, clean_lotsize


def main():

    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    df = clean_price(df)
    df = clean_lotsize(df)
    df = normalize_address(df)
    df = clean_address(df)

    keep_cols = ["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_market"]
    df_new = df[keep_cols]

    df_colnew = df_new.copy()

    df_colnew["price_per_sqft"] = df_colnew["price"] / df_colnew["sqft"] # useful for knowing the price per square foot of the house

    print(df_colnew[["price_per_sqft","price","sqft"]].head())
    print(df_colnew.info())
    print(df_new[["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_market"]].head())
    print(df_new.info())
    
    
if __name__ == "__main__":
    main()
