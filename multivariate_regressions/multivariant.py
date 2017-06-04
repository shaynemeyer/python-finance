import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt


# Run a multivariate regression with 5 independent variables – from Test 1 to Test 5.
data = pd.read_excel('IQ_data.xlsx')
print("==============================================================================")
print(data)
print("==============================================================================")

print("Multivariate Regression:")
print("Independent Variables: Test 1, Test 2, Test 3, Test 4, Test 5")
X = data[['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print("==============================================================================")
print(reg.summary())
print("==============================================================================")

# The p-value of the variable Test 1 in the univariate regression looked very promising.
# Is it still low? If not – what do you think would be the reason for the change?

# Try regressing Test 1 and Test 2 on the IQ score first. Then, regress Test 1, 2, and 3 on IQ, and finally,
# regress Test 1, 2, 3, and 4 on IQ. What is the Test 1 p-value in these regressions?
print("==============================================================================")
print("Independent Variables: Test 1, Test 2")
X = data[['Test 1', 'Test 2']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==============================================================================")
print("==============================================================================")

print("Independent Variables: Test 1, Test 2, Test 3")
X = data[['Test 1', 'Test 2', 'Test 3']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==============================================================================")
print("==============================================================================")
print("Independent Variables: Test 1, Test 2, Test 3, Test 4")
X = data[['Test 1', 'Test 2', 'Test 3', 'Test 4']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==============================================================================")

# It seems it increases a lot when we add the result from Test 4.

# Run a regression with only Test 1 and Test 4 as independent variables.
# How would you interpret the p-values in this case?
print("==============================================================================")
print("Independent Variables: Test 1, Test 4")
X = data[['Test 1', 'Test 4']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==============================================================================")
print("==============================================================================")
print("Independent Variables: Test 4")
X = data[['Test 4']]
Y = data['IQ']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==============================================================================")

print("Suggested Answer: Test 1 and Test 4 are correlated, and they contribute to the preparation of the IQ test in a similar way.")
