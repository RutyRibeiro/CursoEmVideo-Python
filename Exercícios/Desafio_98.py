# programa com função que recebe inicio, fim e passo de uma contagem, a realiza formatada 
from time import sleep

# função responsável por fazer e imprimir a contagem
def contador(inicio,fim,passo):
    print('-'*50)
    print(f'Contando de {inicio} a {fim} de {passo} em {passo}\nContagem:', end='')
    for i in range(inicio,fim+1,passo):
        sleep(0.5)
        print(i,' ' ,end='')
    print('FIM!\n')


# programa principal
contador(0,10,1)
contador(10,0,-2)
print('       \033[33mPERSONALIZE A CONTAGEM!\033[m')
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))