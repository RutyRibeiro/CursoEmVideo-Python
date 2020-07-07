# jokenpo
import random, sys
num=random.randint(0,2)
lista=['PEDRA','PAPEL','TESOURA']
escolha=(input(('\033[33mJokenpô\033[m (Pedra , Papel ou Tesoura)\nDigite sua escolha:'))).upper()
if escolha=='PEDRA' or escolha == 'PAPEL' or escolha =='TESOURA':
    print('\033[34mVocê\033[m: {}\n\033[34mPC\033[m: {}\n\n\033[34m{}\033[m X \033[34m{}\033[m'.format(escolha, lista[num],escolha, lista[num]))
else:
    print('Digite uma opção válida!')
    sys.exit()
if escolha=='PEDRA':
    if lista[num] == 'PEDRA':
        print('\033[33mEmpate\033[m!!!')
    elif lista[num] == 'PAPEL':
        print('\033[33mVocê Perdeu\033[m!!!')
    else:
        print('\033[33mVocê Venceu\033[m!!!')
elif escolha=='PAPEL':
    if lista[num] == 'PAPEL':
        print('\033[33mEmpate\033[m!!!')
    elif lista[num] == 'TESOURA':
        print('\033[33mVocê Perdeu\033[m!!!')
    else:
        print('\033[33mVocê Venceu\033[m!!!')
else:
    if lista[num] == 'TESOURA':
        print('\033[33mEmpate\033[m!!!')
    elif lista[num] == 'PEDRA':
        print('\033[33mVocê Perdeu\033[m!!!')
    else:
        print('\033[33mVocê Venceu\033[m!!!')
