import numpy as np
import pandas as pd
from pandas_datareader import data as web
from scipy.stats import norm
import matplotlib.pyplot as plt

ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='google', start='2007-1-1', end='2017-3-21')['Close']

# Store the annual standard deviation of the log returns in a variable, called “stdev”.
log_returns = np.log(1 + data.pct_change())
print(log_returns.tail())
print("#"*40)

data.plot(figsize=(10, 6));

stdev = log_returns.std() * 250 ** 0.5
print("Standard Deviation: ")
print(stdev)
print("#"*40)
# Set the risk free rate, r, equal to 2.5% (0.025).
r = 0.025
print("#"*40)
# To transform the object into an array, reassign stdev.values to stdev.
type(stdev)
print("Convert standard deviation to an array:")
stdev = stdev.values
print(stdev)
print("#"*20)

# Set the time horizon, T, equal to 1 year, the number of time intervals equal to 250,
# the iterations equal to 10,000. Create a variable, delta_t, equal to the quotient
# of T divided by the number of time intervals.
T = 1.0
t_intervals = 250
delta_t = T / t_intervals
iterations = 10000

# Let Z equal a random matrix with dimension (time intervals + 1) by the number of iterations.
Z = np.random.standard_normal((t_intervals + 1, iterations))

# Use the .zeros_like() method to create another variable, S, with the same dimension as Z.
# S is the matrix to be filled with future stock price data.
S = np.zeros_like(Z)

# Create a variable S0 equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
S0 = data.iloc[-1]
S[0] = S0

# Use the following formula to create a loop within the range (1, t_intervals + 1) that reassigns values to S in time t.

for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

print(S)
print(S.shape)
print("#"*20)

# Plot the first 10 of the 10,000 generated iterations on a graph.
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);