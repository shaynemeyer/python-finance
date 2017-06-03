import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

assets = ['WMT', 'FB']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='google', start='2014-1-1')['Close']

log_returns = np.log(pf_data / pf_data.shift(1))

num_assets = len(assets)

weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
print("==========================================")
# Now, estimate the expected Portfolio Return, Variance, and Volatility.
print("Expected Portfolio Return:")
print(np.sum(weights * log_returns.mean()) * 250)
print("==========================================")
print("Expected Portfolio Variance:")
print(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))
print("==========================================")
print("Expected Portfolio Volatility:")
print(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
print("==========================================")
# 1) Create two empty lists. Name them pf_returns and pf_volatilites.
pf_returns = []
pf_volatilities = []
# 2) Create a loop with 1,000 iterations that will generate random weights, summing to 1,
# and will append the obtained values for the portfolio returns and the portfolio volatilities
# to pf_returns and pf_volatilities, respectively.
for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

print(pf_returns, pf_volatilities)
print("==========================================")
# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites.
# Once you have done that, the two objects will be NumPy arrays.
pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)

print(pf_returns, pf_volatilities)
print("==========================================")
# Now, create a dictionary, called portfolios, whose keys are the strings “Return” and “Volatility” and
# whose values are the NumPy arrays pf_returns and pf_volatilities.
portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_volatilities})
print(portfolios.head())
print("==========================================")
print(portfolios.tail())
print("==========================================")
# Finally, plot the data from the portfolios dictionary on a graph. Let the x-axis represent the volatility
# data from the portfolios dictionary and the y-axis – the data about rates of return.
# Organize your chart well and make sure you have labeled both the x- and the y- axes.
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
print("==========================================")

# What do you think would happen if you re-created the Markowitz Efficient Frontier for 3 stocks? The code you
# have created is supposed to accommodate easily the addition of a third stock, say British Petroleum (‘BP’).
# Insert it in your data and re-run the code (you can expand the “Cell” list from the Jupyter menu and click on
# “Run All” to execute all the cells at once!).
# How would you interpret the obtained graph?
assets = ['WMT', 'FB', 'BP']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='google', start='2014-1-1')['Close']

pf_data.head()
print("==========================================")
log_returns = np.log(pf_data / pf_data.shift(1))
num_assets = len(assets)
print(num_assets)
print("==========================================")
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
print(weights[0] + weights[1] + weights[2])
print("==========================================")
print("Expected Portfolio Return:")
print(np.sum(weights * log_returns.mean()) * 250)
print("==========================================")
print("Expected Portfolio Variance:")
print(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))
print("==========================================")
print("Expected Portfolio Volatility:")
print(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))
print("==========================================")
pfolio_returns = []
pfolio_volatilities = []

for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

print(pfolio_returns, pfolio_volatilities)

portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})

portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')