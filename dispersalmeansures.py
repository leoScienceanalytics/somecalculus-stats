import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
df = pd.read_excel('base pcp.xlsx')


# Cálculo da variância
variancia = np.var(df['QNTD'])

# Cálculo do desvio padrão
desvio_padrao = np.std(df['QNTD'])

# Exibindo os resultados
print('Variância: ', variancia)
print('Desvio Padrão: ', desvio_padrao)


#Estatística descritiva
print(df.describe())


plt.plot(df.index, df['QNTD'], marker='o', linestyle = '-', color='blue')
plt.show()