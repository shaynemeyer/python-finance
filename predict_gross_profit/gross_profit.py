import numpy as np
import matplotlib.pyplot as plt

rev_m = 170
rev_stdev = 20
iterations = 1000

rev = np.random.normal(rev_m, rev_stdev, iterations)
print(rev)

plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

COGS = - (rev * np.random.normal(0.6, 0.1))

plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()

print("COGS Mean:")
print(COGS.mean())

print("COGS Standard deviation:")
print(COGS.std())