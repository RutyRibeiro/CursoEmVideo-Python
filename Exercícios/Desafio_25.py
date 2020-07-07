#lê nome e analisa se existe 'silva'
nome=input(print('Digite o nome:'))
nome=nome.upper()
if ('SILVA' in nome) == True:
    print('Este nome possui silva')
else:
    print('este nome não possui silva')