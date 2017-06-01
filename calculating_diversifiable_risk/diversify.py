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

print("==========================================")

# Diversifiable Risk
COST_var_a = sec_returns[['COST']].var() * 250
print(COST_var_a)
WMT_var_a = sec_returns[['WMT']].var() * 250
print(WMT_var_a)

print("==========================================")
