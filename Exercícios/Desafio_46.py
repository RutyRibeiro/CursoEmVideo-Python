#Gera contagem regressiva de ano novo
from time import sleep
print('CONTAGEM REGRESSIVA')
for i in range(10,-1,-1):
    print('\033[33m{}\033[m'.format(i))
    sleep(1)
print('Feliz ano novo!')