# adaptação do desafio 107 usando função que formata os valores retornados
import moeda

quant=float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(quant)} = {moeda.moeda(moeda.metade(quant))}')
print(f'O dobro de {moeda.moeda(quant)} = {moeda.moeda(moeda.dobro(quant))}')
print(f'A aumentando 15% obtemos: = {moeda.moeda(moeda.aumentar(quant,15))}')
print(f'A diminuindo 35% obtemos: = {moeda.moeda(moeda.diminuir(quant,15))}')
