# gera uma matriz 3x3 e a imprime corretamente, demonstrando linhas e colunas 
from random import randint
matriz=[[],[],[]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(randint(10,20))
for i in range(0,3):
    for j in range(0,3):
        print(f'[ {matriz[i][j]} ] ',end='')
    print('\n')