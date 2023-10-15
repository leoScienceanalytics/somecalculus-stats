def gauss_seidel(A, b, x0, max_iter, tol):
    n = len(A)
    x = x0.copy()

    for _ in range(max_iter):
        x_prev = x.copy()

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]

        # Verifica a condição de parada
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            break

    return x

# Exemplo de uso
A = [[4, 1, 1],
     [2, 7, 1],
     [1, 2, 5]]

b = [7, 4, 1]

x0 = [0, 0, 0]  # Valores iniciais da matriz transposta 0
max_iter = 100  # Número máximo de iterações
tol = 1e-6  # Tolerância para a condição de parada

solucao = gauss_seidel(A, b, x0, max_iter, tol)
print("A solução encontrada é:", solucao)
