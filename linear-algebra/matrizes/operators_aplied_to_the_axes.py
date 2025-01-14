import numpy as np

matriz = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

print(matriz[:, 1])

# operacoes nas colunas
soma_elementos_c2 = matriz[:, 1]. sum()
mult_elementos_c2 = matriz[:, 1].prod()

print(f"Soma Elementos Coluna 2: {soma_elementos_c2}")
print(f"Multiplicação Elementos Coluna 2: {mult_elementos_c2}")


# operacoes nas linhas
soma_elementos_l1 = matriz[0, :]. sum()
mult_elementos_l1 = matriz[0, :].prod()

print(f"Soma Elementos Coluna 2: {soma_elementos_l1}")
print(f"Multiplicação Elementos Coluna 2: {mult_elementos_l1}")


# soma de cada linha de uma matriz
print(matriz.sum(axis=0))

# soma de cada coluna de uma matriz
print(matriz.sum(axis=1))