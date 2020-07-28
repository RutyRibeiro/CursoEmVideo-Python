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
print(pessoas)