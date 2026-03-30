import numpy as np

def portfolio_variance(weights, cov):
    return weights.T @ cov @ weights

def risk_contribution(weights, cov):

    port_var = portfolio_variance(weights, cov)

    marginal = cov @ weights
    rc = weights * marginal / port_var

    return rc