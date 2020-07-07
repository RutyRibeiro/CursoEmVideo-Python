# Recebe número e converte para binario, hexadecimal ou octal
num=int(input('Digite um número: '))
resp=input('1 - Binário\n2 - Octal\n3 - Hexadecimal\nConverter para: ')
if resp == '1':
    print('{} em binário equivale a: {:b}'.format(num,num))
elif resp == '2':
    print('{} em octal equivale a: {:o}'.format(num,num))
else:
    print('{} em hexadecimal equivale a: {:x}'.format(num,num))