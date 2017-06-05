import numpy as np
import matplotlib.pyplot as plt

# Imagine you are an experienced manager and you have forecasted revenues of $200 million,
# with an expected deviation of $10 million. You are convinced Cogs will be near 40% of the revenues,
# and their expected deviation is 20% of its own value.

# Use NumPy’s random.random function to simulate the potential revenue stream for 250 iterations
# (which is the number of trading days in a year) and then the predicted Cogs value.

rev_m = 200
rev_stdev = 10
iterations = 250

rev = np.random.normal(rev_m, rev_stdev, iterations)
print(rev)
print("==============================================================================")
print("Plot the obtained data for revenues and Cogs on a graph and observe the behavior of the obtained values.")
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()
print("==============================================================================")
COGS = - (rev * np.random.normal(0.4, 0.2))

plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()
print("==============================================================================")
print("Cogs mean:")
print(COGS.mean())
print("==============================================================================")
print("Cogs std:")
print(COGS.std())
print("==============================================================================")