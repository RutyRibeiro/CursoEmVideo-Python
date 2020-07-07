# recebe 3 retas e diz se forma triangulo se sim mostra o tipo
r1=int(input('Digite o comprimento da primeira reta:'))
r2=int(input('Digite o comprimento da segunda reta:'))
r3=int(input('Digite o comprimento da terceira reta:'))

if r1+r2<r3 or r3+r2<r1 or r1+r3<r2:
    print('As retas NÃO formam triângulo')
else:
   if r1==r2 and r2==r3:
       print('Triangulo equilátero!')
   elif r1!=r2 and r2!=r3:
       print('Triângulo Escaleno!')
   else:
       print('Triângulo isosceles!')
