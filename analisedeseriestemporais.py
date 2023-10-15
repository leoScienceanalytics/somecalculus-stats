#Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import pacf
import statsmodels.api as sm






# Carregue os dados do arquivo Excel
df = pd.read_excel('NVDA.csv')

# Verifique o formato dos dados carregados
print(df.head())



#Visualizar a série temporal
# Plot da série temporal
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'])
plt.xlabel('Date')
plt.ylabel('Close')
plt.title("Série Temporal")
plt.grid(True)
plt.show()






# Decomposição da série temporal em tendência, sazonalidade e resíduos
decomposicao = seasonal_decompose(df["Close"], model="additive")

# Plot da decomposição
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df.index, df['Close'], label="Original")
plt.legend(loc="best")
plt.subplot(412)
plt.plot(df.index, decomposicao.trend, label="Tendência")
plt.legend(loc="best")
plt.subplot(413)
plt.plot(df.index, decomposicao.seasonal, label="Sazonalidade")
plt.legend(loc="best")
plt.subplot(414)
plt.plot(df.index, decomposicao.resid, label="Resíduos")
plt.legend(loc="best")
plt.tight_layout()
plt.show()





#Preparando Modelo para as previsões
#Definindo o "p, d e q"
# Plot da autocorrelação
plt.figure(figsize=(12, 4))
plot_acf(df["Close"], lags=20)
plt.xlabel("Lags")
plt.ylabel("Autocorrelação")
plt.title("Autocorrelação")
plt.show()

# Plot da autocorrelação parcial
plt.figure(figsize=(12, 4))
plot_pacf(df["Close"], lags=20)
plt.xlabel("Lags")
plt.ylabel("Autocorrelação Parcial")
plt.title("Autocorrelação Parcial")
plt.show()


#Componente Autorregressio (q)
# Valores das defasagens (X(t-1), X(t-2), X(t-3), ...)
defasagens = [1.2, 2.1, 1.8]  # Substitua pelos valores das defasagens adequados

# Coeficientes autorregressivos (φ1, φ2, φ3, ...)
coeficientes_ar = [0.7, -0.3, 0.2]  # Substitua pelos coeficientes autorregressivos adequados

# Constante (c)
constante = 1.5  # Substitua pela constante adequada

# Cálculo do valor atual (X(t))
p= constante + np.dot(coeficientes_ar, defasagens)

print("Componente Autorregressivo (q):", p)

#Componente de Difereniação (d)
serie_temporal = df['Close'] 

# Cálculo do componente de diferenciação
d = np.diff(serie_temporal)

print("Componente de Diferenciação:", d)

#Componente da Média Móvel (q)
serie_temporal = df['Close']  # Substitua pelos valores da sua série temporal

# Janela da média móvel
janela = 29  # Substitua pelo tamanho da janela desejada

# Cálculo da componente de média móvel
q = pd.Series(serie_temporal).rolling(window=janela).mean()

print("Componente de média móvel:", q)




# Ajustando o modelo ARIMA na série temporal
modelo = ARIMA(df["Close"], order=(p, d, q))  # Substitua p, d e q pelos valores adequados
modelo_treinado = modelo.fit()




# Previsões para um período futuro
horizonte = 10  # Número de períodos para fazer previsões
previsoes = modelo_treinado.forecast(steps=horizonte)

# Exibindo as previsões
print(previsoes)

# Plot das previsões
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"], label="Série Temporal")
plt.plot(previsoes.index, previsoes, label="Previsões")
plt.xlabel("Date")
plt.ylabel("Close")
plt.title("Previsões usando ARIMA")
plt.legend(loc="best")
plt.grid(True)
plt.show()


