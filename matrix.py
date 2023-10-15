import pandas as pd
import numpy as np

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 4, 6, 8, 10],
    'D': [10, 8, 6, 4, 2],
    'E': [4, 6, 8, 10, 12]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print(df)
print(correlation_matrix)
