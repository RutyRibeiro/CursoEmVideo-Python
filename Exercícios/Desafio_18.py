#receber angulo e calcular seno cosseno e tangente
from math import sin,cos,tan
ang=float(input(print('Digite um ângulo: ')))
print('Ângulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang,sin(ang),cos(ang),tan(ang)))