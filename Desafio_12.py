#recebe o preço de um produto e calcula seu novo preço com 5% de desconto
preco=float(input(print('Digite o preço: ')))
print('O novo preço é: R${:.2f}'.format(preco-((5/100)*preco)))
