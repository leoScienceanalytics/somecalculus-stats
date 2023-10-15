import numpy as np
import pandas as pd

df = pd.read_csv('NVDA.csv')

x = df['Open']
y = df['Close']

correlation = np.corrcoef(x, y)
correlation_xy = correlation[0,1]

#Similar ao do Doc "Correlação.py"
print(correlation_xy)
