# analisa se frase digitada é palindroma ou nao
frase = (((input('Digite uma frase: ')).replace(' ', ''))).upper()
frase = list(frase)
cont = 0
for i in range(0, len(frase)):
    if frase[i] != frase[(len(frase) - 1) - i]:
        cont = cont + 1
if cont > 0:
    print('Frase não palíndroma!')
else:
    print('Frase Palíndroma!')
