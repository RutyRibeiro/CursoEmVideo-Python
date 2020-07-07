import random
a1=input(print('Digite o nome do primeiro aluno'))
a2=input(print('Digite o nome do segundo aluno'))
a3=input(print('Digite o nome do terceiro aluno'))
a4=input(print('Digite o nome do quarto aluno'))

lista = [a1,a2,a3,a4]

print('Aluno escolhido é: {}'.format(random.choice(lista)))
