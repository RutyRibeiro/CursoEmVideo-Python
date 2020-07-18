#mostra a tabuada dos numeros digitados termina quando digitado um número negativo 
num=0
while num>=0:
    print('\033[35mTABUADA\033[m')
    num=int(input('Digite um número (negativo para interromper): '))
    if num<0:
        break
    for i in range(0,11):
        print(f'\033[33m{num}\033[m X {i} = {num*i}')
print('Fim')