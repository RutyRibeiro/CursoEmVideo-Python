#recebe dois números e vê qual o maior, se os dois forem iguais gera mensagem de aviso
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
if num1>num2:
    print('\033[34m{}\033[m é maior que \033[34m{}\033[m'.format(num1,num2))
elif num2>num1:
    print('\033[34m{}\033[m é maior que \033[34m{}\033[m'.format(num2,num1))
else:
    print('Os números são iguais!')