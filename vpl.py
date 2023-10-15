#Definir função

def calcular_vlp(valorFuturo, taxaDesconto, periodo):
    vlp = valorFuturo / (1 + taxaDesconto) ** periodo
    return vlp


valorFut = float(input('Valor Futuro: '))
taxaDesconto = float(input('Taxa: '))
periodo = float(input('Período: '))

vlp = calcular_vlp(valorFut, taxaDesconto, periodo)
vlp = round(vlp, 2)



print('Valor Líquido Presente: ', vlp)



