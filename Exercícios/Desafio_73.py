# atraves de uma tupla com a tabela do brasileirão gera informações
tabela=('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama','Atlético Mineiro','Fluminense','Botafogo','Ceará SC','Cruzeiro','CSA','Chapecoense','Avaí')
print('\nBrasileirão 2019\n')
print('\033[33m5 Primeiros colocados\033[m:')
for i in range (0,5):
    print(f'{i+1}° {tabela[i]}')
print('\n\033[33m4 Últimos colocados\033[m:')
for i in range (len(tabela)-4,len(tabela)):
    print(f'{i+1}° {tabela[i]}')
tabela1=sorted(tabela)    
print('\n\033[33mTimes em ordem alfabetica\033[m:')
for i in range (0,len(tabela)):
    print( tabela1[i])

print('\n\033[33m4 Posição do Time Chapecoense\033[m:{}° lugar'.format(int(tabela.index('Chapecoense'))+1))