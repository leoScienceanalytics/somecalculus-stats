import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Criar um conjunto de dados de exemplo
data = {
    'Filme': ['Filme A', 'Filme B', 'Filme C', 'Filme D', 'Filme E'],
    'Enredo': [4, 2, 5, 3, 4],
    'Atuacao': [5, 3, 4, 2, 3],
    'Direcao': [3, 4, 4, 5, 2],
    'TrilhaSonora': [2, 4, 3, 1, 5]
}

df = pd.DataFrame(data)
print(df)

# Selecionar apenas as colunas numéricas para a análise de clusters
X = df.drop('Filme', axis=1)

# Normalizar os dados
X = (X - X.mean()) / X.std()

# Aplicar o algoritmo K-means para formar 3 clusters
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
df['Cluster'] = kmeans.fit_predict(X)

# Visualização dos clusters em um gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df['Enredo'], df['Atuacao'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Enredo')
plt.ylabel('Atuação')
plt.title('Clusters de Avaliações de Filmes')


for i, row in df.iterrows():
    plt.annotate(row['Filme'], (row['Enredo'], row['Atuacao']), textcoords="offset points", xytext=(0,10), ha='center')


plt.show()



# Exibir a atribuição de clusters para cada filme
print(df[['Filme', 'Cluster']])



