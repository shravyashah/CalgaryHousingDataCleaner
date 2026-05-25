import pandas as pd

def main():

    df = pd.read_csv("data/raw/data_ab.csv", low_memory = False)
    
    keep_cols = ["addressLocality", "addressRegion", "price", "property-beds", "property-baths"]
    df_new = df[keep_cols]


    print(df_new.head(10))
    print(df_new.info())
    print(df_new.isna().sum())

if __name__ == "__main__":
    main()
