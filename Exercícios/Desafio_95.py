# aprimoramento do exercicio 93, capaz de analizar o aproveitamento de varios jogadores
dic={}
apoio=[]
lista=[]
esc='S'
forma='{:-^85}'.format('-')
while esc=='S':  
    dic['Nome']=input('Digite o nome do jogador: ').capitalize()
    dic['Partidas jogadas']=int(input(f'Quantidade de partidas jogadas por {dic["Nome"]}:'))
    for i in range (0,dic['Partidas jogadas']):
        num=int(input(f'Gols na partida {i}: '))
        apoio.append(num)
    dic['Gols']=apoio[:]
    dic['Total de gols']=sum(dic['Gols']) 
    lista.append(dic.copy())
    dic.clear()
    apoio.clear()     
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção válida!')
        esc=(input('Deseja continuar [S/N]:')).upper()
    print(forma)

print('\033[33m{:^85}\033[m\n{}'.format('APROVEITAMENTO',forma))
print('\033[33m{:<5} {:<60}{:<7}{:>10}\033[m\n{}'.format('COD','NOME','GOLS','TOTAL',forma))
for i,v in enumerate(lista):
    print('{:<5} {:<60}{}{:>10}'.format(i,v['Nome'],v['Gols'],v['Total de gols']))
print(forma)

while True:
    esc=int(input('Deseja ver os dados de qual jogador(a)? [999 interrompe]: '))
    if esc==999:
        break
    elif esc<0 or esc>=len(lista):
        print('\nCódigo de jogador(a) inválido!')
    else:    
        print(f'\nJogador(a) {lista[esc]["Nome"]} jogou {lista[esc]["Partidas jogadas"]} partidas em que:')
        for i,v in enumerate(lista[esc]['Gols']):
            print(f'--> Na partida {i} fez {v} gols')    
    print('\n')

