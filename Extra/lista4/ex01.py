def menor(n1,n2):
    if n1 == n2:
        print('Os números são iguais!')
    elif n1<n2:
        print(f'O primeiro número é menor!')
    else:
        print(f'O segundo número é menor!')

try:
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    menor(n1,n2)
except Exception as e:
    print(f'Houve um erro: {e}')
    
