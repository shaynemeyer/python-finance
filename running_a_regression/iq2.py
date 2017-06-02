import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Computing Alpha, Beta, and R Squared in Python


data = pd.read_excel('IQ_data.xlsx')

X = data['Test 1']
Y = data['IQ']

plt.scatter(X, Y)
plt.axis([0, 120, 0, 150])
plt.ylabel('IQ')
plt.xlabel('Test 1')
plt.show()

# Use the statsmodels’ .add_constant() method to reassign the X data on X1.
# Use OLS with arguments Y and X1 and apply the fit method to obtain univariate
# regression results. Help yourself with the .summary() method.
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())
print("==========================================")
# By looking at the p-values, would you conclude Test 1 scores are a good predictor?

# Imagine a kid would score 84 on Test 1. How many points is she expected to get on the IQ test, approximately?

print(45 + 84*0.76)
print("==========================================")
# Alpha, Beta, R^2:
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
print("Slope:")
print(slope)
print("==========================================")
print("Intercept:")
print(intercept)
print("==========================================")
print("r value:")
print(r_value)
print("==========================================")
print("r value squared:")
print(r_value ** 2)
print("==========================================")
print("p value:")
print(p_value)
print("==========================================")
print("standard error:")
print(std_err)
print("==========================================")
# Use the values of the slope and the intercept to predict the IQ score of a child,
# who obtained 84 points on Test 1. Is the forecasted value different than the one you obtained above?
print("Use the values of the slope and the intercept to predict the IQ score of a child, who obtained 84 points on Test 1. Is the forecasted value different than the one you obtained above?")
print(intercept + 84 * slope)
print("==========================================")

# Follow the steps to draw the best fitting line of the provided regression.
# Define a function that will use the slope and the intercept value to calculate the dots of the best fitting line.
def fitline(b):
    return intercept + slope * b

line = fitline(X)

plt.scatter(X,Y)
plt.plot(X,line)
plt.show()
