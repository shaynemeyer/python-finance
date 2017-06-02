import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['MSFT', 'AAPL']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='google', start='2007-1-1')['Close']

print(sec_data)

print("==========================================")
# Then, calculate the diversifiable and the non-diversifiable risk of a portfolio, composed of these two stocks:
sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns)

print("==========================================")
weights = np.array([0.5, 0.5])
# Portfolio Variance:
print("Portfolio Variance:")
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print(pfolio_var)


# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio
print("==========================================")
print("Diversifiable Risk:")
MSFT_var_a = sec_returns['MSFT'].var() * 250
print(MSFT_var_a)

AAPL_var_a = sec_returns['AAPL'].var() * 250
print(AAPL_var_a)

# Calculating Diversifiable Risk:
print("==========================================")
print("Calculating Diversifiable Risk:")
dr = pfolio_var - (weights[0] ** 2 * MSFT_var_a) - (weights[1] ** 2 * AAPL_var_a)
print(dr)
print(str(round(dr*100, 3)) + ' %')

# Calculating Non-Diversifiable Risk:
print("==========================================")
print("Calculating Non-Diversifiable Risk:")
n_dr_1 = pfolio_var - dr
print(n_dr_1)
# or
n_dr_2 = (weights[0] ** 2 * MSFT_var_a) + (weights[1] ** 2 * AAPL_var_a)
print(n_dr_2)

# Calculating Portfolio Variance
weights_2 = np.array([0.2, 0.8])
print("==========================================")
print("Portfolio Variance:")
pfolio_var_2 = np.dot(weights_2.T, np.dot(sec_returns.cov() * 250, weights_2))
print(pfolio_var_2)

# Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio
print("==========================================")
print("Calculating Diversifiable Risk:")
dr_2 = pfolio_var - (weights_2[0] ** 2 * MSFT_var_a) - (weights_2[1] ** 2 * AAPL_var_a)
print(dr_2)

print(str(round(dr*100, 3)) + ' %')

print("==========================================")
print("Calculating Non-Diversifiable Risk:")
n_dr_2 = pfolio_var - dr_2
print(n_dr_2)
