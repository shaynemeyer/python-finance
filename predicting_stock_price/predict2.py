import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='google', start='2000-1-1')['Close']

log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

# Use “.values” to transform the drift and the stdev objects into arrays.
print(type(drift))
print(drift.values)
print(type(stdev))

# Forecast future stock prices for every trading day a year ahead. So, assign 250 to “t_intervals”.
# Let’s examine 10 possible outcomes. Bind “iterations” to the value of 10.

t_intervals = 250
iterations = 10

# Use the formula we have provided and calculate daily returns.
# daily_returns = exp(drift + stdev∗z),

# where z = norm.ppf(np.random.rand(t_intervals, iterations)

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print(daily_returns)
