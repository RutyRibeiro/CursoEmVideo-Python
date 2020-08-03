# Programa com duas funções a primeira responsavel por carregar uma lista com numeros aleatorios e a segunda somará os números pares contidos na variavel composta  
from random import randint
from time import sleep
lista=[]
somaPares=0

#Função que sorteia números para a lista 
def sorteio(lista):
    print('SORTEANDO VALORES PARA A LISTA: ', end='')
    for i in range(0,5):
        sleep(0.5)
        lista.append(randint(0,50))
        print(lista[i], ' ', end='')
    print('FIM!')

# função de soma dos numeros pares
def soma(lista,somaPares):
    for v in lista:
        if v % 2 ==0 :
            somaPares=somaPares+v
    print(f'Somando os valores pares obtemos: {somaPares}')


# programa principal
sorteio(lista)
soma(lista,somaPares)