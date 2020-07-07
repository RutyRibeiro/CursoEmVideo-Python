#recebe altura e largura de uma parede e calcula quantidade de tinta necessária
alt=float(input(print('Digite a altura da parede: ')))
larg=float(input(print('Digite a largura da parede: ')))
area=alt*larg

quant=area/2

print('Parede: {} X {} \nÁrea: {}'.format(alt,larg,area))

print('A quantidade de tinta necessaria para pintar essa area é: {:.2f} Litros'.format(quant))