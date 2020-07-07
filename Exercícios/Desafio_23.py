# Lê numero de até 4 digitos e mostra unidade por unidade
num=input(print('Digite um numero de 4 digitos:'))
tam= len(num)
if tam<=4:
    if tam==0:
        print('Digite um número!')
    else:
        print('Unidade = {}'.format(num[tam-1]))
    if tam>=2:
        print('Dezena = {}'.format(num[tam-2]))
        if tam>=3:
            print('Centena = {}'.format(num[tam-3]))
            if tam==4:
                print('Milhar= {}'.format(num[tam-4]))
else:
    print('Digite um número de até 4 digitos!')