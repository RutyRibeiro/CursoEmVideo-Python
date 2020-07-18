#par ou ímpar jogo só será interrompido quando o jogador perder, mostrará a quantidade de vitorias consecutivas 
from random import randint
vit=True
vitorias=0
while vit!=False:
    esc=input('Digite 1 para par e 2 para ímpar: ')
    numJog=int(input('Digite o seu número (de 0 á 10): '))
    numpc=randint(0,10)
    num=numJog+numpc
    print(f'\nSeu número: {numJog}\nNúmero do PC: {numpc}\nTotal = {num}\n')
    if num%2==0:
        print('Resultado: \033[33mPAR!\033[m\n')
    else:
        print('Resultado: \033[33mÍMPAR!\033[m\n')
    if esc=='1' or esc=='2':
        if esc=='1':
            if num%2==0:
                print("Você ganhou!")
                vitorias+=1
            else:
                print("Você Perdeu!")
                vit=False
        else:
            if num%2==0:
                print("Perdeu!")
                vit=False
            else:
                print("Ganhou!")
                vitorias+=1
    else:
        print('Digite uma opção Válida!')
print(f'Você ganhou {vitorias} vezes seguidas')
