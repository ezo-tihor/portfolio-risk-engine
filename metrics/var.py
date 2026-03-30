import numpy as np
import pandas as pd

def historical_var(returns : pd.Series, alpha = 0.05) -> float:
    '''
    VaR tells the maximum loss I can expect with X% confidence. In this case it'll
    calculate the cutoff for (100 - X) percentile?
    '''
    return np.percentile(returns, 100*alpha)