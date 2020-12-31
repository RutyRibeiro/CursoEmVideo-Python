def modulo(n1):
    n2=abs(n1)
    return n2

try:
    n1=float(input('Digite o seu número'))
    n2 = modulo(n1)
    print(f'O módulo do seu número é: {n2}')
except Exception as e:
    print(f'Houve um erro: {e}')
    
