import pandas as pd
import numpy as np

def cvar(returns : pd.Series, alpha = 0.05) -> float:
    '''
    cvar calculates the avg of the tails beyond var
    '''
    var = np.percentile(returns, 100*alpha)
    return returns[returns <= var].mean()

