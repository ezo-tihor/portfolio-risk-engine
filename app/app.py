
# st.title('Portfolio Risk Dashboard')
# st.write('Coming Soon...')

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import utils
import core
import metrics
import risk


# CONFIG
#---------------------

DATA_PATH = 'data/prices.csv'
TICKERS = ['SPY', 'TLT', 'GLD', 'QQQ'] #S&P500, Long term US government bonds, Gold ETF, NASDAQ100

st.set_page_config(layout='wide')
st.title('Portfolio Risk Dashboard')

#---------------------
# LOAD DATA
#---------------------

if os.path.exists(DATA_PATH):
    print('Loading cached data...')
    prices = utils.data_loader.load_prices(DATA_PATH)
else:
    print('Fetching new data...')
    prices = utils.data_fetcher.fetch_prices(TICKERS)
    prices.to_csv(DATA_PATH)

returns = utils.returns.compute_returns(prices, 'normal')

#---------------------
# SIDEBAR INPUTS
#---------------------

st.sidebar.header('Portfolio Weights')
weights = [] 
for ticker in TICKERS: #Normalize this part later on so that sum of weights = 1.0
    w = st.sidebar.slider(ticker, 0.0, 1.0, 0.25)
    # print(type(w))
    weights.append(w)

weights = np.array(weights)

#Normalize (important)
if weights.sum() == 0:
    st.error('Weights cannot all be zero')
    st.stop()

weights = weights / weights.sum()

#---------------------
# PORTFOLIO
#---------------------

portfolio_obj = core.portfolio.Portfolio(weights, returns)
portfolio_returns = portfolio_obj.portfolio_returns()


#---------------------
# METRICS
#---------------------

var = metrics.var.historical_var(portfolio_returns)
cvar = metrics.cvar.cvar(portfolio_returns)
drawdown, max_dd = metrics.drawdown.drawdown(portfolio_returns)

cov_matrix = risk.covariance.covariance_matrix(returns)
risk_contribution = risk.risk_contribution.risk_contribution(portfolio_obj.weights, cov_matrix)



#---------------------
# DISPLAY
#---------------------

col1, col2, col3 =st.columns(3)

col1.metric('VaR (5%)', f"{var:.4f}")
col2.metric('CVaR', f"{cvar:.4f}")
col3.metric('Max Drawdown', f"{max_dd:.4f}")



#---------------------
# CHARTS
#---------------------

st.subheader('Portfolio returns')
st.line_chart(portfolio_returns)

st.subheader('Drawdown')
st.line_chart(drawdown)


#---------------------
# RISK CONTRIBUTION
#---------------------

st.subheader('Risk Contribution')

risk_contribution_dict = {ticker : float(val) for ticker, val in zip(TICKERS, risk_contribution)}
st.bar_chart(risk_contribution_dict)


st.subheader("Correlation Matrix")
corr = returns.corr()
st.dataframe(corr)