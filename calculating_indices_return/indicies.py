import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^FTSE']
ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='google', start='1997-1-1')['Close']

print(ind_data.head())

print(ind_data.tail())

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

ind_returns = (ind_data / ind_data.shift(1)) - 1
print(ind_returns.tail())

annual_ind_returns = ind_returns.mean() * 250
print(annual_ind_returns)

tickers = ['MSFT', '^GSPC', '^DJI']

data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(t, data_source='google', start='2007-1-1')['Close']

print(data_2.tail())