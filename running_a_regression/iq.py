import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

# A teacher at school decided her students should take an IQ test.
# She prepared 5 tests she believed were aligned with the requirements
# of the IQ examination. The father of one child in the class turned out
# to be an econometrician, so he asked her for the results of the 30 kids.
# The file contained the points they earned on each test and the final IQ score.

# Load the IQ_data excel file.
data = pd.read_excel('IQ_data.xlsx')
print(data)
print("==========================================")
# Prepare the data for a univariate regression of Test 1 based on the IQ result.
# Store the Test 1 scores in a variable, called X, and the IQ points in another variable, named Y.
print(data[['IQ', 'Test 1']])
print("==========================================")

# Univariate Regression
print("Univariate Regression")
print("==========================================")

X = data['Test 1']
Y = data['IQ']

print(X)
print(Y)

# Create a well-organized scatter plot. Use the “axis” method with the following start and end points:
# [0, 120, 0, 150]. Label the axes “Test 1” and “IQ”, respectively.

plt.scatter(X,Y)
plt.axis([0, 120, 0, 150])
plt.ylabel('IQ')
plt.xlabel('Test 1')
plt.show()