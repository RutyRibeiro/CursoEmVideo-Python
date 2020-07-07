# lê a velocidade de um carro caso a velocidade ultrapasse o permitido calcula a multa por km
velocidade=float(input('Digite a velocidade: '))
if velocidade> 80:
    print('VOCÊ FOI MULTADO! Preço: R$:{:.2f}'.format((velocidade-80)*7.00))
else:
    print('Parabéns você se manteve na velocidade correta!')