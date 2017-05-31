import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

MSFT = wb.DataReader('MSFT', data_source='google', start='2000-1-1')

print(MSFT.head())

print(MSFT.tail())

MSFT['simple_return'] = (MSFT['Close'] / MSFT['Close'].shift(1)) - 1
print(MSFT['simple_return'])

MSFT['simple_return'].plot(figsize=(8,5))
plt.show()

# Daily rate of return
avg_returns_d = MSFT['simple_return'].mean()
print("Daily Rate of Return:", avg_returns_d)

# Annual rate of return
avg_returns_a = MSFT['simple_return'].mean() * 250
print("Annual Rate of Return:", avg_returns_a)

# Annual rate of return percentage
print(str(round(avg_returns_a, 5) * 100) + ' %')