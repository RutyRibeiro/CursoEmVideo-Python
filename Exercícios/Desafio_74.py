#incrementa 5 numeros aleatorios para uma tupla, mostra maior e menor
from random import randint
tupla=(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
maior=tupla[0]
menor=tupla[0]
print('Os elementos gerados para a tupla são:')
for i in range(0, len(tupla)):
    print(tupla[i])
    if tupla[i]> maior:
        maior=tupla[i]
    if tupla[i]< menor:
        menor=tupla[i]
print(f'O maior e menor elemento da tupla são, respectivamente: {maior} e {menor}')    


