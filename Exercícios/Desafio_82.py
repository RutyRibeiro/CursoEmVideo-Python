# recebe numeros, após carrega duas listas derivadas com os numeros pares e impares 
lista=[]
pares=[]
impares=[]
esc='S'
while esc=='S':    
    lista.append(int(input('Digite um número: ')))
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção valida!')
        esc=(input('Deseja continuar [S/N]:')).upper()
    print('\n')
for v in lista:
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print('Elementos cadastrados: {}\nElementos pares: {}\nElementos ímpares: {}'.format(lista,pares,impares))