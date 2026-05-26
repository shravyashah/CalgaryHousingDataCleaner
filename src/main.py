import pandas as pd
from clean import clean_price

def main():

    df = pd.read_csv("data/raw/calgary_houses_raw.csv", low_memory = False)
    
    #keep_cols = ["address","bedrooms","bathrooms","price","sqft","lot_size", "garage","community","property_type","days_on_markert"]
    #df_new = df[keep_cols]
    
    df = clean_price(df)
    print(df.head())
    print(df["price"])
    
    
    
if __name__ == "__main__":
    main()
