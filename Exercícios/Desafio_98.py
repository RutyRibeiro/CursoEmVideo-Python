# programa com função que recebe inicio, fim e passo de uma contagem, a realiza formatada 

from time import sleep

# função responsável por fazer e imprimir a contagem
def contador(inicio,fim,passo):
    # transforma o passo em 1 caso o recebido seja 0
    if passo==0:
        passo=1
    # corrige o passo caso a contagem seja regressiva e o passo esteja positivo ou transforma
    if fim < inicio and passo>0:
        passo*=-1
    print('-'*50)
    print(f'Contando de {inicio} á {fim} de {abs(passo)} em {abs(passo)}\nContagem:', end='')
    # a estrutura condicional contida na função range faz com que todos os números propostos sejam incluidos na contagem 
    for i in range(inicio, fim+1 if fim > inicio else fim-1,passo):
        sleep(0.5)
        print(i,' ' ,end='')
    print('FIM!\n')


# programa principal
contador(0,10,1)
contador(10,0,-2)
print('       \033[33mPERSONALIZE A CONTAGEM!\033[m')
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))