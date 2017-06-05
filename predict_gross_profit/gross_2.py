import numpy as np
import matplotlib.pyplot as plt

rev_m = 200
rev_stdev = 10
iterations = 256

rev = np.random.normal(rev_m, rev_stdev, iterations)
COGS = - (rev * np.random.normal(0.4,0.2))
print("==============================================================================")
print("COGS mean:")
print(COGS.mean())
print("COGS Standard deviation:")
print(COGS.std())
print("==============================================================================")
# Based on the predicted revenue and Cogs values, estimate the expected Gross Profit of your company.
# Reminder: Be careful about estimating the gross profit. If you have stored the Cogs value as a negative
# number, the gross profit will equal revenues plus Cogs. If you have created Cogs as a positive value,
# then gross profit would be equal to revenues minus Cogs. Either way, you will obtain the same result for
# gross profit.
print("==============================================================================")
print("Gross Profit:")
Gross_Profit = rev + COGS
print(Gross_Profit)
print("==============================================================================")
plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()
print("==============================================================================")
print("Max gross profit: ")
print(max(Gross_Profit))
print("==============================================================================")
print("Min gross profit:")
print(min(Gross_Profit))
print("==============================================================================")
# What is its mean and standard deviation?
print("Gross profit mean:")
print(Gross_Profit.mean())
print("==============================================================================")
print("Gross profit standard deviation:")
print(Gross_Profit.std())
print("==============================================================================")
# Do you remember what a histogram is? Plot the gross profit data on a histogram.
# Use 20 bins directly to check the distribution of the data.
plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins=20)
plt.show()
print("==============================================================================")