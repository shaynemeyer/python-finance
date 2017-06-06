import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

# Download the data for Microsoft (‘MSFT’) from Google Finance for the period ‘2000-1-1’ until today.
ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='google', start='2000-1-1')['Close']

# Use the .pct_change() method to obtain the log returns of Microsoft for the designated period.
log_returns = np.log(1 + data.pct_change())
print(log_returns.tail())

data.plot(figsize=(10, 6))

log_returns.plot(figsize=(10, 6))
print("==============================================================================")
data.plot(figsize=(10, 6))
print("==============================================================================")
log_returns.plot(figsize=(10, 6))
# Assign the mean value of the log returns to a variable, called “U”,
# and their variance to a variable, called “var”.

u = log_returns.mean()
print(u)
print("==============================================================================")
var = log_returns.var()
print(var)
print("==============================================================================")
# Calculate the drift, using the following formula:
print("Drift:")
drift = u - (0.5 * var)
print(drift)
print("==============================================================================")
# Store the standard deviation of the log returns in a variable, called “stdev”.
print("Standard deviation:")
stdev = log_returns.std()
print(stdev)


