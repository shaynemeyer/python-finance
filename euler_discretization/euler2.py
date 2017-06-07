import numpy as np
import pandas as pd
from pandas_datareader import data as web
from scipy.stats import norm
import matplotlib.pyplot as plt

ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='google', start='2000-1-1')['Close']

log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std() * 250 ** 0.5
stdev = stdev.values

r = 0.025
T = 1.0
t_intervals = 250
delta_t = T / t_intervals
iterations = 10000

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0

for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])


plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);

# Use numpy.maximum to create a vector with as many elements as there are columns in the S matrix.
p = np.maximum(S[-1] - 110, 0)

# numpy.maximum() will create an array that contains either 0s or the numbers equal to the differences

print(p)
print(p.shape)
print("#"*20)
# Use the following formula to forecast the price of a stock option.
print("#"*20)
print("Sum p:")
print(np.sum(p))
print("#"*20)
C = np.exp(-r * T) * np.sum(p) / iterations
print(C)
print("#"*20)




