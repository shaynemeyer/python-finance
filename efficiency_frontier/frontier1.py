import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Begin by extracting data for Walmart and Facebook from the 1st of January 2014 until today.
assets = ['WMT', 'FB']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source='google', start = '2014-1-1')['Close']

print(pf_data.tail())

print((pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5)))

# Calculate their logarithmic returns.
log_returns = np.log(pf_data / pf_data.shift(1))

# Create a variable that carries the number of assets in your portfolio.
num_assets = len(assets)
print(num_assets)

# The portfolio need not be equally weighted. So, create a variable,
# called “weights”. Let it contain as many randomly generated values as
# there are assets in your portfolio. Don’t forget these values should be neither
# smaller than 0 nor equal or greater than 1!
# Hint: There is a specific NumPy function that allows you to generate such values.
# It is the one we used in the lecture - NumPy.random.random().
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)

# Sum the obtained values to obtain 1 – summing up the weights to 100%!
print(weights[0] + weights[1])