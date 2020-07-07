#sortear nome de um dos quatro alunos de um professor
import random
a1=input(print('Digite o nome do primeiro aluno'))
a2=input(print('Digite o nome do segundo aluno'))
a3=input(print('Digite o nome do terceiro aluno'))
a4=input(print('Digite o nome do quarto aluno'))
sort=random.randint(1,4)
if sort==1:
    print('Aluno sorteado é: {}'.format(a1))
else:
    if sort ==2:
        print('Aluno sorteado é: {}'.format(a2))
    else:
        if sort==3:
            print('Aluno sorteado é: {}'.format(a3))
        else:
            print('Aluno sorteado é: {}'.format(a4))