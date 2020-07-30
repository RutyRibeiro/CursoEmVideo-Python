# recebe nome e duas notas de alunos, gera boletim com média de todos, apos isso possibilita ver as notas individuais de cada aluno
apoio=[]
lista=[]
esc='S'
forma='{:-^75}'.format('-')
while esc=='S':    
    apoio.append(input('Digite o nome do aluno: '))
    apoio.append(int(input('Digite a 1ª nota: ')))
    apoio.append(int(input('Digite a 2ª nota: ')))
    lista.append(apoio[:])
    apoio.clear()
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção valida!')
        esc=(input('Deseja continuar [S/N]:')).upper()
print(forma)
print('{:^75}'.format('BOLETINS'))
print(forma)
print('\033[33m{:<5} {:<60}{:>7}\033[m'.format('N°','NOME','MÉDIA'))
print(forma)
for i in range(0,len(lista)):
    print('{:<5} {:<60}{:>7.2f}'.format(i,lista[i][0],(lista[i][1]+lista[i][2])/2))
print(forma)
while True:
    esc=int(input('Deseja ver as notas de qual aluno? [999 interrompe]: '))
    if esc==999:
        break
    else:
        print(f'As notas do aluno: \033[34m{lista[esc][0]}\033[m são: {lista[esc][1]} e {lista[esc][2]}')
    print('\n')