import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['BP', 'F', 'XOM', 'LNC', 'AAPL']

mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='google', start='2000-1-1')['Close']

print(mydata.info())

print(mydata.head())

print(mydata.iloc[0])

(mydata / mydata.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

returns = (mydata / mydata.shift(1)) - 1
print(returns.head())

annual_returns = returns.mean() * 250
print(annual_returns)

weights = np.array([0.20, 0.20, 0.20, 0.20, 0.20])
print(np.dot(annual_returns, weights))

portfolio1 = str(round(np.dot(annual_returns, weights), 5) * 100) + '%'
print(portfolio1)