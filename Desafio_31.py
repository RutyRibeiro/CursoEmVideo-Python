# Calcula o preço da passagem de onibus de acordo com a distancia em km
dist=float(input('Digite a distancia em KM da viagem:'))
if dist<=200:
    print('O preço da viagem é: R${:.2f}'.format(dist*0.50))
else:
    print('O preço da viagem é: R$:{:.2f}'.format(dist*0.45))