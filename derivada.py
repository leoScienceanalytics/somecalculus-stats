from sympy import symbols, diff #symbol --> usada para transformar variáveis simbólica/ diff --> usada para cálcular a derivada simbólica

# Definição da variável simbólica e da função
x = symbols('x')

função = 19*x**5 + 20*x**3 + 1

# Cálculo da derivada
derivada = diff(função, x)

# Imprimindo o resultado
print("Derivada:", derivada)
