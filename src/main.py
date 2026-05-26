import pandas as pd
from clean import clean_price,clean_address


def main():

    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    keep_cols = ["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_market"]
    df_new = df[keep_cols]
    
    df_new = clean_price(df_new)
    df_new = clean_address(df_new)
    print(df_new.head())
    print(df_new["price"])
    print(df_new["address"])
    
    
if __name__ == "__main__":
    main()
