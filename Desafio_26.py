# le frase, conta a quantidade de 'a', onde esta a primeira e a ultima
frase=input(print('Digite algo:'))
frase=frase.replace(' ','')
frase=frase.lower()
print('Quantidade de a: {}'.format(frase.count('a')))
print('O primeiro A é {}ª letra'.format(frase.find('a')+1))
print('O último A é {}ª letra'.format(frase.rfind('a')+1))
