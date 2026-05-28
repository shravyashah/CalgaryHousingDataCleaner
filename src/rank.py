import pandas as pd
from features import create_price_per_sqft, ranking_price_per_sqft_system

def normalize(series):
    return (series - series.min()) / (series.max() - series.min()) if series.max() != series.min() else 0

def score_houses(df):
    df = df.copy()  # Avoid modifying the original DataFrame

    return df


