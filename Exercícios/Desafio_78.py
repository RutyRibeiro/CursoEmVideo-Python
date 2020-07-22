# recebe 5 valores para uma lista, calcula maior e menor capturando suas respectivas posições
lista=[]
for i in range(0,5):
    lista.append(int(input('Digite o {} número: '.format(i+1))))
maior=lista[0]
menor=lista[0]
for v in lista:
    if v > maior:
        maior=v
    if v < menor:
        menor=v
print(f'O maior valor é {maior} encontrado na(s) posição(ões): ',end='')
for i in range(0,len(lista)):
    if lista[i]==maior:
        print(i)
print(f'O menor valor é {menor} encontrado na(s) posição(ões): ',end='')
for i in range(0,len(lista)):
    if lista[i]==menor:
        print(i)
