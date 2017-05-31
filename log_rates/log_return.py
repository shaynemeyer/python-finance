import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

MSFT = wb.DataReader('MSFT', data_source='google', start='2000-1-1')

# print(MSFT.head())
#
# print(MSFT.tail())

MSFT['log_return'] = np.log(MSFT['Close'] / MSFT['Close'].shift(1))
print(MSFT['log_return'])

MSFT['log_return'].plot(figsize=(8,5))
plt.show()

# Daily rate of return
log_returns_d = MSFT['log_return'].mean()
print(log_returns_d)

# Annual rate of return
log_returns_a = MSFT['log_return'].mean() * 250
print(log_returns_a)

# Annual rate of return percentage
print(str(round(log_returns_a, 5) * 100) + ' %')