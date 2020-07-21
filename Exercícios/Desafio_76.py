#monta tabela de preços a partir de uma tupla 
tabela=('Pão Francês',0.77,'Leite',2.79,'café',10,'maçã',1,'Banana',11,'Miojo',1.50,'Torrada',5,'Ovo',11,'Abacate',2)
print('{:-^70}'.format('-'))
print('{:^70}'.format('TABELA DE PREÇOS'))
print('{:-^70}'.format('-'))
for i in range(0,len(tabela),2):
    print('{:.<60}R${:>7.2f}'.format(tabela[i],tabela[i+1]))
print('{:-^70}'.format('-'))