import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregue os dados em um DataFrame do Pandas
df = pd.read_excel('Base teste.xlsx')





# Calcule a média e a amplitude

media = df['Quantidade'].mean()
media = round(media, 2)

amplitude = df['Quantidade'].max() - df['Quantidade'].min()
amplitude = round(amplitude, 2)


desvioPadrao = np.std(df['Quantidade'])
desvioPadrao = round(desvioPadrao, 2)


print('Média: ', media)
print('Amplitaude:', amplitude) 
print('Desvio Padrão', desvioPadrao)







# Limites de controle Média
A2 = 0.135
limite_superior_media = media + (A2 * amplitude)
limite_superior_media = round(limite_superior_media, 2)

limite_inferior_media = media - (A2 * amplitude)
limite_inferior_media = round(limite_inferior_media, 2)


print('Limite Superior de Controle da Média: ', limite_superior_media)
print('Limite Inferior de Controle da Média: ', limite_inferior_media)









# Limites de controle Amplitude
D3 = 0.459
D4 = 1.541
limite_superior_amplitude = amplitude * D4
limite_superior_amplitude = round(limite_superior_amplitude, 2)

limite_inferior_amplitude = amplitude * D3
limite_inferior_amplitude = round(limite_inferior_amplitude, 2)

print('Limite Superior de Controle da Amplitude: ', limite_superior_amplitude)
print('Limite Inferior de Controle da Amplitude: ', limite_inferior_amplitude)








    
#Gráfico de controle Média

plt.plot(df.index, df["Quantidade"], marker="o", linestyle="-", color="blue")
plt.axhline(y=media, color="red", linestyle="--", label="Média")
plt.axhline(y=limite_superior_media, color="orange", linestyle="-.", label="Limite Superior de Controle da Média")
plt.axhline(y=limite_inferior_media, color="purple", linestyle="-.", label="Limite Inferior de Controle da Média")
plt.legend()


for i, valor in enumerate(df["Quantidade"]):
    plt.plot([i, i], [valor, 1], color="gray", linestyle=":", linewidth=0.5)
    plt.text(i, -0.5, f"X{i}", ha="center", fontsize=6)



plt.xlabel("Período")
plt.ylabel("Quantidade")
plt.title("Gráfico de Controle da Média")
plt.show()








#Gráfico de Controle Amplitude

plt.plot(df.index, df["Quantidade"], marker="o", linestyle="-", color="blue")
plt.axhline(y=amplitude, color="red", linestyle="--", label="Amplitude")
plt.axhline(y=limite_superior_amplitude, color="orange", linestyle="-.", label="Limite Superior de Controle da Amplitude")
plt.axhline(y=limite_inferior_amplitude, color="purple", linestyle="-.", label="Limite Inferior de Controle da Amplitude")
plt.legend()

for i, valor in enumerate(df["Quantidade"]):
    plt.plot([i, i], [valor, 1], color="gray", linestyle=":", linewidth=0.5)
    plt.text(i, -0.5, f"X{i}", ha="center", fontsize=6)



plt.xlabel("Período")
plt.ylabel("Quantidade")
plt.title("Gráfico de Controle da Amplitude")
plt.show()


