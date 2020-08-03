#Programa com função que recebe valores e mostra a quantidade e o maior entre eles  
 
from time import sleep

def maior(*valores):
    print(70*'-')
    print(f'Foram recebidos {len(valores)} valores, estes são: ', end='')
    for v in valores:
        sleep(0.5)
        print(v,' ', end='')
    print(f'\nDentre estes o maior valor é: {max(valores)}') 


# programa principal
maior(0,8,6,9,34,24,67)
maior(1,2,3,4,9,5)
maior(10,9,35,56,54,23,653)