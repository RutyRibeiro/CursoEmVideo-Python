def negativo (n1):
    if n1< 0:
        print('Número negativo!')
    elif n1 == 0:
        print('Número neutro!')
    else:
        print('Número positivo!')

try:
    n1=int(input('Digite seu número: '))
    negativo(n1)
except Exception as e:
    print(f'Houve um erro: {e}')
