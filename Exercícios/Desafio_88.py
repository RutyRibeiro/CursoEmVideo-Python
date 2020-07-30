# sorteia números (de 1 a 60) para a quantidade de jogos recebida
from random import randint
from time import sleep
lista=[]
apoio=[]
num=int(input('Digite a quantidade de jogos: '))
print('{:>25}'.format('SORTEANDO NÚMEROS'))
for i in range(0,num):
    sleep(1)
    for j in range(0,6):
        apoio.append(randint(1,60))
    print(f'Jogo {i+1}: {apoio}')
    lista.append(apoio[:])
    apoio.clear()
