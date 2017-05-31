import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

MSFT = wb.DataReader('MSFT', data_source='google', start='2000-1-1')

print(MSFT.head())

print(MSFT.tail())

MSFT['simple_return'] = (MSFT['Close'] / MSFT['Close'].shift(1)) - 1
print(MSFT['simple_return'])