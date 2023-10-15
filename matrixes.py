def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(2):
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def calcular_soma_linhas(matriz):
    soma_linhas = []
    for linha in matriz:
        soma = sum(linha)
        soma_linhas.append(soma)
    return soma_linhas


def calcular_soma_total(matriz):
    soma_total = sum(sum(linha) for linha in matriz)
    return soma_total


def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)


def main():
    matriz = ler_matriz()
    soma_linhas = calcular_soma_linhas(matriz)
    soma_total = calcular_soma_total(matriz)

    print("Soma de cada linha da matriz:")
    for soma in soma_linhas:
        print(soma)

    print("Soma total dos elementos da matriz:", soma_total)
    print("Matriz:")
    imprimir_matriz(matriz)


main()


