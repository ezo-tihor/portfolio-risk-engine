import numpy as np
import pandas as pd

class Portfolio:
    def __init__(self, weights, returns : pd.DataFrame):
        self.weights = np.array(weights)
        self.returns = returns

        self._validate()

    
    def _validate(self):
        if not np.isclose(np.sum(self.weights), 1):
            raise ValueError("Weights must sum to 1")
        
        if len(self.weights) != self.returns.shape[1]:
            raise ValueError("Weights must match number of assets")
        
    
    def portfolio_returns(self) -> pd.Series:
        return self.returns @ self.weights
    
    def mean_return(self) -> float:
        return self.portfolio_returns().mean()
    
    def volatility(self) -> float:
        return self.portfolio_returns().std()




        