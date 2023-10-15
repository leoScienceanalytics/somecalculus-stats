import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import datetime
import seaborn as sns

df = pd.read_csv('NVDA.csv')

df['Date'] = pd.to_datetime(df['Date']) #Necessário, pois todas as colunas do gráfico serão analisadas.


close = df['Close']
adjClose = df['Adj Close']


correlation, p_value = pearsonr(close, adjClose)

correlationPearson = df.corr()


print('Coeficiente de Correlação: ', correlation)
print('Valor-p: ', p_value)
print('Coeficiente Correlação de Pearson: ', correlationPearson)



#Gráfico da Correlação de Pearson
plt.imshow(correlationPearson, cmap='RdYlBu', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlationPearson.columns)), correlationPearson.columns)
plt.yticks(range(len(correlationPearson.columns)), correlationPearson.columns)
plt.show()

