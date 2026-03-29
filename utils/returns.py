import numpy as np
import pandas as pd

def compute_returns(prices : pd.DataFrame, method = 'log') -> pd.DataFrame:
    if method == 'log':
        return np.log(prices / prices.shift(1))
    else:
        returns = prices.pct_change()

    return returns.dropna()