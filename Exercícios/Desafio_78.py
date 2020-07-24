# recebe 5 valores para uma lista, calcula maior e menor capturando suas respectivas posições
lista=[]
for i in range(0,5):
    lista.append(int(input('Digite o {} número: '.format(i+1))))
maior=lista[0]
posiMaior=[]
menor=lista[0]
posiMenor=[]
for v in lista:
    if v > maior:
        maior=v
    if v < menor:
        menor=v
for i in range(0,len(lista)):
    if lista[i]==maior:
        posiMaior.append(i)
    if lista[i]==menor:
        posiMenor.append(i)
print(f'O menor valor é {menor} encontrado na(s) posição(ões): ',end='')
i=0
for i in range(0, len(posiMenor)):
    print(posiMenor[i],'',end='')
print(f'\nO maior valor é {maior} encontrado na(s) posição(ões): ',end='')
i=0
for i in range(0, len(posiMaior)):
    print(posiMaior[i],'',end='')