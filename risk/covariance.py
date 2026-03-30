import numpy as np
import pandas as pd

def covariance_matrix(returns : pd.DataFrame) -> np.ndarray:
    '''
    Input is the returns for the tickers and it computes covariance matrix for the assets (N*N dimension)
    and returns it as a numpy array (N*N)
    '''
    print('oze')
    return returns.cov().values