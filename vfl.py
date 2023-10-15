def calcular_vfl(valorPresente, taxaDesconto, periodo):
    vfl = valorPresente * (1 + taxaDesconto) ** periodo
    return vfl

valorPresente = float(input('Valor presente: '))
taxaDesconto = float(input('Taxa: '))
periodo = float(input('Período: '))

vlf = calcular_vfl(valorPresente, taxaDesconto, periodo)
vlf = round(vlf, 2)

print('Valor Líquido Futuro', vlf)
