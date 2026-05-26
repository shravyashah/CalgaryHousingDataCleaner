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

    print(df_new.head(13))
    print(df_new.info())
    
    
if __name__ == "__main__":
    main()
