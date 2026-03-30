import pandas as pd
import numpy as np

def drawdown(returns : pd.Series):

    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    dd = (cumulative - peak)/peak

    max_drawdown = dd.min()
    return dd, max_drawdown