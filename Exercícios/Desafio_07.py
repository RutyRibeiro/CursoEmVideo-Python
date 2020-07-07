#Calcular média entre duas notas de um aluno
nome=input('Nome do aluno: ')
nota1=float(input(print('Digite a primeira nota: ')))
nota2=float(input(print('Digite a segunda nota: ')))
media = (nota1+nota2) / 2

print('A média de {} é igual a: {}'.format(nome,media))

if media >= 5:
    print('Situação: Aprovado')
else:
    print('Situação: Exame')