# calcula a soma entre impares multiplos de 3 entre 1 e 500
soma=0
for i in range(1,501):
    if i%3==0 and i%2!=0:
        soma= soma+i
print('A soma de todos os numeros impares multiplos de 3 (entre 1 e 500) equivale a: \033[34m{}'.format(soma))