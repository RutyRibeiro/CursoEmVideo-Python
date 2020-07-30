# gera e mostra matriz 3x3, no final mostra: a soma dos valores pares, soma dos valores da terceira coluna e o maior valor da linha 2
from random import randint
matriz=[[],[],[]]
somaPares = somaTerc = 0
for i in range(0,3):
    for j in range(0,3):
        num=randint(10,20)
        matriz[i].append(num)
        if num%2==0:
            somaPares+=num
        if j==2:
            somaTerc+=num
for i in range(0,3):
    for j in range(0,3):
        print(f'[ {matriz[i][j]} ] ',end='')
    print('\n')
print(f'A soma de todos os valores pares da matriz é igual a: {somaPares}\nA soma dos valores da terceira coluna é igual a: {somaTerc}\nO maior valor da segunda linha é: {max(matriz[1])}')
