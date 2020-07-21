#Recebe 4 valores, os coloca numa tupla, calcula quant de '9', posição do primeiro 3 e quantidade de pares
v1=int(input('Digite o 1° valor: '))
v2=int(input('Digite o 2° valor: '))
v3=int(input('Digite o 3° valor: '))
v4=int(input('Digite o 4° valor: '))
tupla=(v1,v2,v3,v4)
quantPares=0
pares=''
i=0
while i<len(tupla):
    if tupla[i] % 2 == 0:
        quantPares+=1
        pares=('{} {}'.format(pares, tupla[i]))
    i+=1   
if 3 in tupla==True:
    print('O primeiro 3 está na posição: {}'.format(tupla.index(3)+1))
else:
    print('O número 3 não está nesse conjunto de números!')
print('Total de números 9 digitados: {}\nA quantidade de pares é: {} São eles: {}'.format(tupla.count(9),quantPares,pares))