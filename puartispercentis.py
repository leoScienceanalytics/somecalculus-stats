import pandas as pd
import numpy as np

# Dados de exemplo
df = pd.read_excel('base pcp.xlsx')

# Cálculo dos quartis
quartis = np.percentile(df['QNTD'], [25, 50, 75])

# Cálculo de percentis
percentis = np.percentile(df['QNTD'], [10, 30, 60, 90])

# Exibindo os resultados
print("Quartis:", quartis)
print("Percentis:", percentis)
