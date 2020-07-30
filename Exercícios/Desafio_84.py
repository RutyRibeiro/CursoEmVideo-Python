# cadastra nomes e pesos de pessoas em uma lista a partir de uma lista de apoio, no final mostra quantidade de pessoas cadastradas maior e menor pesos e os respectivos nomes atribuidos 
apoio=[]
pessoas=[]
esc='S'
while esc=='S':    
    apoio.append(input('Digite o nome: '))
    apoio.append(int(input('Digite o peso: ')))
    pessoas.append(apoio[:])
    apoio.clear()
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção valida!')
        esc=(input('Deseja continuar [S/N]:')).upper()
    print('\n')
mini=pessoas[0][1]
maxi=pessoas[0][1]
for i in range(0,len(pessoas)):
    if pessoas[i][1]<mini:
        mini=pessoas[i][1]
    if pessoas[i][1]>maxi:
        maxi=pessoas[i][1]
print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'O peso \033[33mmáximo\033[m foi: {maxi:.2f} de: ',end='')
for i in range(0,len(pessoas)):
    if pessoas[i][1]==maxi:
        print(f'{pessoas[i][0]}',end=', ') 
print(f'\nO peso \033[33mmínimo\033[m foi: {mini:.2f} de: ',end='')
for i in range(0,len(pessoas)):
    if pessoas[i][1]==mini:
        print(f'{pessoas[i][0]}',end=', ') 

