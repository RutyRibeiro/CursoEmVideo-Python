# Joga o dado para 4 jogadores guarda o resultado em um dicionario organizando-o do menor para o menor, mostra a classificação de acordo com a classificação  
from random import randint
from time import sleep
from operator import itemgetter
dic={}
i=1
for i in range(0,4):
    print('{:>20}'.format(f'JOGANDO DADO PARA JOGADOR {i}...'))
    sleep(1)
    dic[f'Jogador{i}']=randint(1,6)
    print(f'\033[33mResultado\033[m: {dic[f"Jogador{i}"]}')
dic = dict(sorted(dic.items(), key=itemgetter(1),reverse=True))
print('\033[34m{:>20}\033[m'.format('CLASSIFICAÇÃO'))
for k,v in dic.items():
    sleep(1)
    print(f'\033[33m{i}°\033[m Lugar: {k} com: {v}')
    i+=1
    