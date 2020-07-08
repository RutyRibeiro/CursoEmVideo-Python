# gera um número entre 0 e 5 e compara com o numero recebido
import random
num=random.randint(0,5)
num1=int(input('digite um número: '))
if num1 == num:
    print('Parabens! O número é: {}'.format(num))
else:
    print('Perdeu! O número é: {}'.format(num))