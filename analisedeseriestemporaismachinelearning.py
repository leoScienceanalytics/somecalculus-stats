#Importando bibliotecas necessárias

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt







#Carregando base de dados

df =  pd.read_csv('NVDA.csv')





#Divindo dados em clusters de treinamento e clusters de teste

X = df['Open']  # Recursos (variáveis independentes)
y = df['Close']  # Variável alvo (demanda)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)





#Treinamento do modelo

model = LinearRegression()
model.fit(X_train, y_train)





#Aplicando modelo

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)





#Gráfico de previsão

plt.plot(y_test, label='Close Real')
plt.plot(y_pred, label='Close forecast')
plt.legend()
plt.show()