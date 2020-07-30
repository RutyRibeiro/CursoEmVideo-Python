from random import randint
from time import sleep
dic={}
for i in range(0,4):
    dic[f'nome{i}']=input(f'Digite o nome do {i+1}° jogador: ').capitalize()
    print('{:>20}'.format('JOGANDO DADO...'))
    sleep(1)
    dic[f'resul{i}']=randint(1,6)
    print(f'\033[33mResultado\033[m: {dic[f"resul{i}"]}')
print(dic)
