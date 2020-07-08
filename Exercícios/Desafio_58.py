# melhoramento do desafio 28 usando função while
import random
num=random.randint(0,10)
num1=11
cont=1
while num1!=num:
    if cont>=2:
        print('Errou!')
        num1=int(input('Digite outro número:'))
    else:
        num1=int(input('Digite um número:'))
    cont+=1   
print('\033[33mParabéns, você acertou!\033[m O número é: {}\nO número total de tentativas é: {}'.format(num,cont-1))
