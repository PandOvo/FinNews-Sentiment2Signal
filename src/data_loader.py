import pandas as pd
from .config import NEWS_FILE, MARKET_FILE

def load_news():
    df = pd.read_csv(NEWS_FILE)
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

def load_market():
    df = pd.read_csv(MARKET_FILE)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df = df.sort_values('date').reset_index(drop=True)
    return df
