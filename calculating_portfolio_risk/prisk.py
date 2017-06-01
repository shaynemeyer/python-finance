import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['COST', 'WMT']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='google', start='2007-1-1')['Close']

print(sec_data.tail())

sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns)
print("==========================================")
# Costco
# Daily
print(sec_returns['COST'].mean())

# Annual
print(sec_returns['COST'].mean() * 250)

# Standard Deviation
print(sec_returns['COST'].std())

#  Annual Standard Deviation
print(sec_returns['COST'].std() * 250 ** 0.5)

print("==========================================")

# Walmart

# Daily
print(sec_returns['WMT'].mean())

# Annual
print(sec_returns['WMT'].mean() * 250)

#
print(sec_returns['WMT'].std())

#
print(sec_returns['WMT'].std() * 250 ** 0.5)

print("==========================================")
print(sec_returns['COST'].mean() * 250)
print(sec_returns['WMT'].mean() * 250)
print("==========================================")
# print(sec_returns['COST', 'WMT'].mean() * 250)

print(sec_returns[['COST', 'WMT']].mean() * 250)
print("==========================================")
print(sec_returns[['COST', 'WMT']].std() * 250 ** 0.5)
print("==========================================")

# Covariance and Correlation
print("Covariance and Correlation")
print("==========================================")
print("Costco variance: ")
COST_var = sec_returns['COST'].var()
print(COST_var)

print("Walmart variance: ")
WMT_var = sec_returns['WMT'].var()
print(WMT_var)

print("==========================================")
print("Costco variance annually: ")
COST_var_a = sec_returns['COST'].var() * 250
print(COST_var_a)

print("Walmart variance annually: ")
WMT_var_a = sec_returns['WMT'].var() * 250
print(WMT_var_a)

print("==========================================")
cov_matrix = sec_returns.cov()
cov_matrix


print("==========================================")
cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a

print("==========================================")
corr_matrix = sec_returns.corr()
corr_matrix

# Calculating Portfolio Risk

# Equal weighting scheme
weights = np.array([0.5, 0.5])

print("Portfolio Variance:")
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print(pfolio_var)

print("Portfolio volatility:")
pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
print(pfolio_vol)

print("==========================================")
print(str(round(pfolio_vol, 5) * 100) + ' %')