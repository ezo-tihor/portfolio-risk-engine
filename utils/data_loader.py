import pandas as pd

def load_prices(path : str) -> pd.DataFrame:
    '''
    Loads data from local csv file. Index = 'Date'. Index is sorted.
    '''
    df = pd.read_csv(path, parse_dates=['Date'], index_col='Date')
    df = df.sort_index()
    df = df.ffill().dropna()

    return df