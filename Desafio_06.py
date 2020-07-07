#Lê número e mostra seu dobro, triplo e raiz quadrada
from math import sqrt,floor
num=int(input(print('Digite um número')))
print('Dobro: {} \nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(num*2,num*3,floor(sqrt(num))))