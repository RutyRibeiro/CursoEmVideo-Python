#Calcula quantidade a pagar por carro alugado
dias=int(input(print('Digite a quantidade de dias alugado: ')))
km=float(input(print('Digite a quantidade de km percorridos')))

print('Total dias: R${:.2f}\nTotal em quilometros: R${:.2f}\nPreço a pagar:{:.2f}'.format(dias*60,km*0.15,dias*60+km*0.15))