#le nome idade e sexo de 4 pessoas e mostra observações especificas
soma_idade=0
idade_homem=0
nome_homem=''
mulheres_menores=0
for i in range(0,4):
    print('\033[33m{}° pessoa\033[m'.format(i+1))
    nome=input('Digite o nome: ')
    idade=int(input('Digite a idade: '))
    sexo=(input('Digite o sexo F/M')).upper()
    soma_idade=soma_idade+idade
    if sexo == 'F':
        if idade<20:
            mulheres_menores=mulheres_menores+1
    else:
        if i == 0:
            idade_homem=idade
        else:
            if idade>idade_homem:
                idade_homem=idade
                nome_homem=nome
print('A média do grupo é de: {} anos'.format(soma_idade/4))
print('O nome do homem mais velho é: {}'.format(nome_homem))
print('A quantidade de mulheres com idade abaixo de 20 anos é: {}'.format(mulheres_menores))

