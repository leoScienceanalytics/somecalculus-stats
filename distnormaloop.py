#Bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np

class Distribuição:
    def __init__(self, media, desvp):#Objeto onde as variáveis retornadas são os próprios parâmetros do construtor
        self.media = media
        self.desvp = desvp
        
    def plot(self, num_point=124): #Função plotagem
        valores = df['Numero'] #define 1000 valores aleatórios a partir da distribução normal, seguindo os parâmetros adotados
        print(valores)
        
        
        plt.figure(figsize=(8,6))
        plt.hist(valores, bins=30, density=True, alpha=0.6, color='orange') #Gráfico de Histograma
        
        xmin, xmax = plt.xlim() #Limites da amostra
        x = np.linspace(xmin, xmax, 124) #Cria 1000 espaçamentos seguindo os parâmetros adotados
        p = stats.norm.pdf(x, self.media, self.desvp) #Calcula os valores da densidade de probalidade     
        plt.plot(x, p, self.media, self.desvp) #Plotagem da curva de distribuição

        title = 'Distribuição Normal da Média = %.2f, Desvio Parão %.2f' % (self.media, self.desvp)
        plt.title(title)
        plt.show()
    

df = pd.read_excel('Teste.xlsx')

media = df['Numero'].mean()
desvp = np.std(df['Numero'])

print('Média:', media)
print('Desvio Padrão:', desvp)
        
        
dist_plot = Distribuição(media, desvp) # x = self.media = 5.015, y = self.desvp = 0.01
dist_plot.plot()

