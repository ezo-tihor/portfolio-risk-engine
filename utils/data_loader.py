import pandas as pd

def load_prices(path : str) -> pd.DataFrame:

    df = pd.read_csv(path, parse_dates=['Date'], index_col='Date')
    df = df.sort_index()
    df = df.ffill().dropna()
    
    return df