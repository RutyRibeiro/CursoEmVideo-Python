# faz o gerenciamento do aproveitamento de um jogador. Recebe nome, quantidade de partidas jogadas e gols feitos em cada partida, tudo é armazenado em um dicionario, inclusive a lista com os gols feitos em todas as partidas
dic={}
apoio=[]
dic['Nome']=input('Digite o nome do jogador: ').capitalize()
dic['Partidas jogadas']=int(input(f'Quantidade de partidas jogadas por {dic["Nome"]}:'))
for i in range (0,dic['Partidas jogadas']):
    num=int(input(f'Gols na partida {i}: '))
    apoio.append(num)
dic['Gols']=apoio
dic['Total de gols']=sum(dic['Gols'])
print('\033[33m{:^75}\033[m'.format('APROVEITAMENTO'))
print('{:-^75}'.format('-'))
for k, v in dic.items():
    print(f'{k}: {v}')
print('{:-^75}'.format('-'))
print(f'Jogador(a) {dic["Nome"]} jogou {dic["Partidas jogadas"]} em que:')
for i,v in enumerate(dic['Gols']):
    print(f'--> Na partida {i} fez {v} gols')
