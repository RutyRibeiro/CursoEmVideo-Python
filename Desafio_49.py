#Calcula a tabuada do numero recebido usando o for
num=int(input('Digite um número: '))
for i in range(11):
    print('{} x {} = {}'.format(num,i,i*num))