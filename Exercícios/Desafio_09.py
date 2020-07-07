#Calcula a tabuada do numero recebido
num=int(input(print('Digite um número: ')))
for i in range(11):
    print('{} x {} = {}'.format(num,i,i*num))