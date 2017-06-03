import numpy as np
import pandas as pd
import quandl

# Let S&P 500 act as the market.
readdata = pd.read_csv('CAPM-Data.csv')

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = readdata[t]

print(data)

# Calculate the beta of Microsoft.
sec_returns = np.log(data / data.shift(1))

cov = sec_returns.cov() * 250
print(cov)

cov_with_market = cov.iloc[0,1]
print(cov_with_market)

market_var = sec_returns['^GSPC'].var() * 250
print(market_var)

PG_beta = cov_with_market / market_var
print(PG_beta)