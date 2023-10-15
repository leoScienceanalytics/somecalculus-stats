from scipy.integrate import quad

def função(x):
    return x**2 + 2*x + 1

limite_inferior = 0
limite_superior = 2

resultado, erro =  quad(função, limite_inferior, limite_superior)
print('Valor da Integral: ', resultado)
print('Valor do Erro: ', erro)

