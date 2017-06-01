import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['MSFT', 'AAPL']

data = pd.DataFrame()

for t in tickers:
    data[t] = wb.DataReader(t, data_source='google', start='2000-1-1')['Close']

returns = np.log(data / data.shift(1))
print(returns)

# MSFT Daily risk:
print(returns['MSFT'].std())

# MSFT Annual risk:
print(returns['MSFT'].std() * 250 ** 0.5)

# Apple Daily risk:
print(returns['AAPL'].std())

# Apple Annual risk:
print(returns['AAPL'].std() * 250 ** 0.5)

vols = returns[['MSFT', 'AAPL']].std() * 250 ** 0.5
print(vols)