import numpy as np
from numpy.linalg import solve

qtd_incognitas = int(input("Digite o número de incógnitas do seu sistema linear\n"))
qtd_equacoes = int(input("Digite o número de equações do seu sistema linear\n"))

matriz = []

for i in range(qtd_equacoes):
    linha = []
    for j in range(qtd_incognitas):
         valor = float(input(f'Digite o valor do elemento [{i+1},{j+1}]: '))
         linha.append(valor)
    
    matriz.append(linha)


print("Matriz do sistema linear:")
for linha in matriz:
     print(linha)

    
b = []
for k in range(qtd_equacoes):
     valor_b = float(input(f'Digite o termo independente da equação {k+1}: '))
     b.append(valor_b)

# Conversão para arrays NumPy
A = np.array(matriz)
b = np.array(b)

x = solve(A, b)

print(f'A solução do sistema linear é {x}')