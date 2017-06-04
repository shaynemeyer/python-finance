import numpy as np
import pandas as pd

# Obtain data for Microsoft and S&P 500 for the period 1st of January 2012 – 31st of December 2016 from Yahoo Finance. Let S&P 500 act as the market. Calculate the beta of Microsoft.
# Assume a risk-free rate of 2.5% and a risk premium of 5%.
# Estimate the expected return of Proctor & Gamble.

readdata = pd.read_csv('CAPM-Data.csv')

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = readdata[t]

print(data)

sec_returns = np.log(data / data.shift(1))
cov = sec_returns.cov() * 250
cov_with_market = cov.iloc[0, 1]
market_var = sec_returns['^GSPC'].var() * 250

PG_beta = cov_with_market / market_var
PG_er = 0.025 + PG_beta * 0.05
print("==========================================")
Sharpe = (PG_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)
print("Sharpe ratio:")
print(Sharpe)
print("==========================================")