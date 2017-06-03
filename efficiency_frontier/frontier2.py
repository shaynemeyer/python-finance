import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

assets = ['WMT', 'FB']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='google', start='2014-1-1')['Close']

log_returns = np.log(pf_data / pf_data.shift(1))

num_assets = len(assets)
print("weights:")
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
print("==========================================")
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
print("Expected Portfolio Return:")
print(np.sum(weights * log_returns.mean()) * 250)
print("==========================================")
# Expected Portfolio Variance:
print("Expected Portfolio Variance:")
print("==========================================")
print(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))
print("==========================================")
print("Expected Portfolio Volatility:")
print(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))
print("==========================================")
# 1) Create two empty lists. Name them pf_returns and pf_volatilites.
pfolio_returns = []
pfolio_volatilities = []

# 2) Create a loop with 1,000 iterations that will generate random weights, summing to 1,
# and will append the obtained values for the portfolio returns and the portfolio volatilities
# to pf_returns and pf_volatilities, respectively.
for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

print(pfolio_returns, pfolio_volatilities)
print("==========================================")
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

print(pfolio_returns, pfolio_volatilities)
