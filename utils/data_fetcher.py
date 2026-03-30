import yfinance as yf
import pandas as pd
import os

def fetch_prices(tickers, start='2018-01-01', end='2024-01-01') -> pd.DataFrame:
    
    data = yf.download(tickers, start=start, end=end)['Close']
    # Clean data
    data = data.ffill().dropna()
    return data


