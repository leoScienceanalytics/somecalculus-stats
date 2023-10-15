import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('Teste.xlsx')

media = df['Numero'].mean()
media = round(media, 2)
print(media)

desvio_padrao = stats.tstd(df['Numero'])
desvio_padrao = round(desvio_padrao, 2)
print(desvio_padrao)

maximo = df['Numero'].max()
print('Max: ', maximo)
minimo = df['Numero'].min()
print('Min: ',minimo)
numeroDaAmostra = len(df['Numero'])
print('Len: ',numeroDaAmostra)


#Gráfico da Distribuição Normal

valores=df['Numero']


plt.figure(figsize=(8,6))
plt.hist(valores, bins=30, density=True, alpha=0.6, color='red')

xmin, xmax = plt.xlim()

# Gerar dados para o eixo x
x = np.linspace(xmin, xmax, 124)

# Calcular os valores da distribuição normal para os dados gerados
y = stats.norm.pdf(x, media, desvio_padrao)

plt.plot(x, y, media, desvio_padrao)

 

# Adicionar rótulos e título
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
title = 'Distribuição Normal da Média = %.2f, Desvio Parão %.2f' % (media, desvio_padrao)
plt.title(title)


# Mostrar o gráfico
plt.show()


