#Recebe algo e testa a natureza do conteudo utilizando a função 'is'
l1 = input(print('Digite algo: '))

if l1.isnumeric() == True:
    print('Apenas números')
else:
    if l1.isalpha() == True:
        print('Apenas letras')
        if l1.isupper() == True:
            print('Todas as letras são maiusculas')
        else:
            if l1.islower()==True:
                print('Todas as letras são minusculas')
            else:
                print('Letras maiúsculas e minusculas')
    else:
        if l1.isalnum() == True:
            print('Possui números e letras')
        else:
            if l1.isspace() == True:
                print('Apenas espaços')
            else:
                print('Não possui nada')

