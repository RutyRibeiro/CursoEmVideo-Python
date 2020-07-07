#calcula imc
peso=float(input('Digite o peso: '))
alt=float(input('Digite a altura: '))
imc=peso/(alt*alt)
print('\033[34mIMC\033[m: {:.2f}'.format(imc))

if imc<18.5:
    print('Abaixo do peso!')
elif imc>=18.5 and imc<25:
    print('Peso ideial! ')
elif imc>=25 and imc<30:
    print('Sobrepeso!')
elif imc>=30 and imc<=40:
    print('Obesidade!')
elif imc>=40:
    print('Obesidade mórbida!')