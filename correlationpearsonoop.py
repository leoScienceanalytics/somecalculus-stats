import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import pearsonr
import datetime

class Correlation:
    def __init__(self, correlationPearson):
        self.correlationPearson = correlationPearson
                
    def plot(self):
        plt.figure(figsize=(8,6))
        plt.imshow(correlationPearson, cmap='RdYlBu', interpolation='nearest')
        plt.colorbar()
        plt.xticks(range(len(correlationPearson.columns)), correlationPearson.columns)
        plt.yticks(range(len(correlationPearson.columns)), correlationPearson.columns)
        plt.show()


        
df = pd.read_csv('NVDA.csv')

df['Date'] = pd.to_datetime(df['Date']) #Necessário, pois todas as colunas do gráfico serão analisadas.


close = df['Close']
adjClose = df['Adj Close']


correlation, p_value = pearsonr(close, adjClose)

correlationPearson = df.corr()


print('Coeficiente de Correlação: ', correlation)
print('Valor-p: ', p_value)
print('Coeficiente Correlação de Pearson: ', correlationPearson)


correlacao = Correlation(correlationPearson)
correlacao.plot()



        
        
        