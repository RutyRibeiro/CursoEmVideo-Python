# calcula preço de produto de acordo com a condição de pagamento
preco = float(input('Digite o preço do produto: R$'))
cond = input('Condição de pagamento: \n1 - A vista (cheque/dinheiro) \n2 - A vista no cartão \n'
             '3 - Em até duas vezes no cartão de crédito\n4 - 3x ou mais no cartão de crédito\n Opção: ')
if cond == '1':
    print('Preço: R${:.2f} com desconto de 10%'.format(preco - ((10 / 100) * preco)))
elif cond == '2':
    print('Preço: R${:.2f} com desconto de 5%'.format(preco - ((5 / 100) * preco)))
elif cond == '3':
    print('Preço: R${:.2f}'.format(preco))
else:
    print('Preço: R${:.2f} com juros de 20%'.format(preco + ((20 / 100) * preco)))
