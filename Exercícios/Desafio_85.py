#recebe 7 números em uma lista, são armazenados em duas listas internas diferentes caso seja par ou ímpar 
lista=[],[]
for i in range(0,7):
    num=int(input(f'Digite o {i+1}° número: '))
    if num%2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Números pares da lista: {lista[0]}\nNúmeros ímpares da lista: {lista[1]}')
