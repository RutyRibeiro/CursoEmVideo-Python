# recebe 3 retas e diz se forma ou não um triangulo
r1=int(input('Digite o comprimento da primeira reta:'))
r2=int(input('Digite o comprimento da segunda reta:'))
r3=int(input('Digite o comprimento da terceira reta:'))

if r1+r2<r3 and r3+r2<r1 and r1+r3<r2:
    print('As retas NÃO formam triângulo')
else:
    print('As retas podem formar um triângulo')