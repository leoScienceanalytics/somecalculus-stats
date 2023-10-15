import math

numero = float(input('Número: '))
base = float(input('Base: '))

log = math.log(numero, base)
log = round(log, 2)

print('Logaritimo de', numero, 'na base', base, 'o resultado é: ', log)

