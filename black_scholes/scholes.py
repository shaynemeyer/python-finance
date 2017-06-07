import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.
ticker = 'MSFT'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='google', start='2000-1-1')['Close']


def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


def d2(S0, K, r, sigma, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))

# Store the annual standard deviation of the log returns in a variable, called “stdev”.
log_returns = np.log(1 + data.pct_change())

log_returns.tail()
print("==========================================")
stdev = log_returns.std() * 250 ** 0.5
print(stdev)
print("==========================================")
# Set the risk free rate, r, equal to 2.5% (0.025); the strike price, K, equal to 110.0; and the time horizon, T, equal to 1, respectively.
r = 0.025
K = 110.0
T = 1
print("==========================================")
# Create a variable S equal to the last adjusted closing price of Microsoft. Use the “iloc” method.
S = data.iloc[-1]
print(S)

print("==========================================")

# Call the d1 and d2 functions with the relevant arguments to obtain their values.
print("D1:")
print(d1(S, K, r, stdev, T))
print("D2:")
print(d2(S, K, r, stdev, T))

print("==========================================")
# Use the BSM function to estimate the price of a call option, given you know the values of S, K, r, stdev, and T.

print(BSM(S, K, r, stdev, T))

