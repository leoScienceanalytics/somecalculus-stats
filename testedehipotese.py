import numpy as np
from scipy import stats

# Dados da amostra
dados = np.array([1, 2, 3, 4, 5])

# Valor de referência
valor_referencia = 3.5

# Realizar o teste t de uma amostra
resultado = stats.ttest_1samp(dados, valor_referencia)

# Exibir o resultado
print("Estatística de teste:", resultado.statistic)
print("Valor-p:", resultado.pvalue)
