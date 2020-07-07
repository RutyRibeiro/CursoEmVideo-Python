# lê nome completo e mostra nome formatação e analise
nome = input(print('Digite o nome completo: '))
maius = nome.upper()
minus = nome.lower()
carac = len(nome.replace(' ', ''))
primer = len(nome.split()[0])

print('Maiuculo: {}\nMinusculo: {}\nTotal de letras: {}\nQuantidade de letras do primeiro nome: {}'.format(maius, minus,
                                                                                                           carac,
                                                                                                           primer))
