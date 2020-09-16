import moeda

quant=float(input('Digite o preço R$: '))
print(f'A metade de R${quant} = {moeda.metade(quant)}')
print(f'O dobro de R${quant} = {moeda.dobro(quant)}')
print(f'A aumentando 15% obtemos: = {moeda.aumentar(quant,15)}')
print(f'A diminuindo 15% obtemos: = {moeda.diminuir(quant,15)}')