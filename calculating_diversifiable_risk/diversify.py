import numpy as np
import pandas as pd
from pandas_datareader import data as wb


tickers = ['COST', 'WMT']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='google', start='2007-1-1')['Close']


sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns)


# Calculating Diversifiable and Nod-diversifiable risk of a portfolio

weights = np.array([0.5, 0.5])

# Portfolio variance
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))

print("==========================================")

# Diversifiable Risk
COST_var_a = sec_returns['COST'].var() * 250
print(COST_var_a)

WMT_var_a = sec_returns['WMT'].var() * 250
print(WMT_var_a)

print("==========================================")
print("Diversifiable Portfolio Risk:")
dr = pfolio_var - (weights[0] ** 2 * COST_var_a) - (weights[1] ** 2 * WMT_var_a)
print(dr)
print(str(round(dr*100, 3)) + ' %')

# Non-Diversifiable Risk:
print("==========================================")
print("Non-Diversifiable Portfolio Risk:")
n_dr_1 = pfolio_var - dr

n_dr_2 = (weights[0] ** 2 * COST_var_a) - (weights[1] ** 2 * WMT_var_a)
print(n_dr_2)

print(n_dr_1 == n_dr_2)
