#lê peso de 5 pessoas mostra maior e menor
maior=0
menor=0
for i in range(0,5):
    peso=float(input('Digite o {}° peso: '.format(i+1)))
    if i==0:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('Maior peso: {}\nMenor peso: {}'.format(maior,menor))
