#Calcular hipotenusa
from math import sqrt,pow,hypot
cato=float(input(print('Cateto Oposto: ')))
cata=float(input(print('Cateto adjacente: ')))
#hipo=sqrt(pow(cata,2)+pow(cato,2))
hipo=hypot(cato,cata)
print('cateto oposto: {}\nCateto Adjacente: {}\nHipotenusa: {:.2f}'.format(cato,cata,hipo))