#Lê quantidade em reais de uma carteira e devolve valor em dólares
real=float(input(print('Digite a quantidade em reais: ')))
dol=real/3.27
print('Você pode comprar US${:.2f}'.format(dol))