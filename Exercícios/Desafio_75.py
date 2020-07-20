#Recebe 4 valores, os coloca numa tupla, calcula quant de '9', posição do primeiro 3 e quantidade de pares
v1=int(input('Digite o 1° valor: '))
v2=int(input('Digite o 2° valor: '))
v3=int(input('Digite o 3° valor: '))
v4=int(input('Digite o 4° valor: '))
tupla=(v1,v2,v3,v4)
pares=0
i=0
while i<len(tupla):
    if tupla[i] % 2 == 0:
        pares+=1
    i+=1   
print('Total de números 9 digitados: {}\nO primeiro 3 foi digitado na posição: {}\nA quantidade de pares é: {}'.format(tupla.count(9),tupla.index(3)+1,pares))
