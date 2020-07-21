# recebe 5 valores para uma lista, calcula maior e menor capturando suas respectivas posições
lista=[]
for i in range(0,5):
    lista.append(int(input('Digite o {} número: '.format(i+1))))
maior=lista[0]
posMaior=[] 
menor=lista[0]
posMenor=[]
for i,v in enumerate(lista):
    if v > maior:
        maior=v
        posMaior.append(i)
    if v < menor:
        menor=v
        posMenor.append(i)
print(f'\nMaior: {maior} está na posição: {posMaior}\nMenor: {menor} está na posição: {posMenor}')