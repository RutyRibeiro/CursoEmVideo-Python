#Calculo de numeros primos
num=int(input('Digite um número: '))
resp=(' 1 {}').format(num)
l=''
for i in range(1, num+1):
    if num%i==0:
        l=('{} {}'.format(l,i))
if l==resp:
    print('Número primo!')
else:
    print("Não é número primo!")