import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

data = pd.read_excel('Housing.xlsx')

data[['House Price', 'House Size (sq.ft.)']]

# Univariate Regression
print("Univariate Regression:")
print("==========================================")
X = data['House Size (sq.ft.)']
Y = data['House Price']

# print(X)
# print(Y)

# plt.scatter(X,Y)
# plt.show()

# plt.scatter(X,Y)
# plt.axis([0, 2500, 0, 1500000])
# plt.show()

plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')
plt.show()