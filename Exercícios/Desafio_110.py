# adaptação do desafio 107 usando função do modulo moeda que gera tabela 
from utilidadesCeV import moeda,dado

quant=dado.leiafloat(input('Digite o preço R$: '))
moeda.resumo(quant, 50,30)