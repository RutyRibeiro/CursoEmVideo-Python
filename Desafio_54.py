#lê ano de nascimento de 7 pessoas mostra quantidade de maiores
maiores=0
menores=0
for i in range(0,7):
    ida=int(input('Digite a {}° idade: '.format(i+1)))
    if ida>=21:
        maiores=maiores+1
    else:
        menores=menores+1
print('Menores: {}\nMaiores: {}'.format(menores,maiores))