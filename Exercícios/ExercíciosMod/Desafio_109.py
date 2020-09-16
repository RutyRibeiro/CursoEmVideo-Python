# adaptação do desafio 107 usando função que formata os valores retornados
import moeda

quant=float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(quant)} = {moeda.metade(quant,True)}')
print(f'O dobro de {moeda.moeda(quant)} = {moeda.dobro(quant,True)}')
print(f'A aumentando 15% obtemos: = {moeda.aumentar(quant,15,True)}')
print(f'A diminuindo 35% obtemos: = {moeda.diminuir(quant,15,True)}')