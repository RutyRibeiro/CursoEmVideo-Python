# cadastra pessoas em dicionarios que posteriormente são adicionados em uma lista, no final mostra média de idade, quantidade de pessoas castradas, nome de todas as mulheres e lista com todas as pessoas com idades acima da média
apoio={}
lista=[]
esc='S'
soma=0
mulheres=''
while esc=='S':    
    apoio['Nome']=(input('Digite o nome: ')).capitalize()
    apoio['Sexo']=(input(f'Digite o sexo de {apoio["Nome"]}: ')).upper()
    while apoio['Sexo']!='F' and apoio['Sexo']!='M':
        print('Digite uma opção valida!')
        apoio['Sexo']=input('Digite o Sexo [F/M]: ').upper()
    apoio['Idade']=(int(input(f'Digite a idade de {apoio["Nome"]} : ')))
    lista.append(apoio.copy())
    apoio.clear()
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção valida!')
        esc=(input('Deseja continuar [S/N]:')).upper()

for v in lista:
    soma += v['Idade']
    if v['Sexo']=='F':
        mulheres=mulheres + ' ' + v['Nome']

print('\033[33m{:>20}\033[m'.format('Informações'))
print(f'Total de pessoas cadastradas: {len(lista)}\nA média de idade: {soma/len(lista)}\nNome de todas as mulheres cadastradas:{mulheres}\nPessoas com idades acima da média:')
for v in lista:
    if v['Idade']> soma/len(lista):
        print(f'{v["Nome"]} com {v["Idade"]} anos.')

