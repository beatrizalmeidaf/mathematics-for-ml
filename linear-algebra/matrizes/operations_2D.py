import numpy as np

A = np.array([
    [2, 4, 7],
    [8, 5, 1],
    [9, 3, 6]
])

B = np.array([
    [5, 2, 1],
    [7, 4, 9],
    [3, 3, 6]
])

soma = A + B
print(soma)

sub = A - B
print(sub)

# mutiplicação entre matrizes: cada elemento da matriz A é multiplicado pelo elemento correspondente da matriz B

mult = A * B
print(mult)

# produto entre matrizes: operação matemática que combina as linhas da primeira matriz com as colunas da segunda matriz.

produto = A.dot(B)
print(produto)

# soma dos elementos da matriz

print(A.sum())


