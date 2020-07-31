# lê a guarda informações pessoais em um dicionário, caso a carteira de trabalho seja diferente de 0 coleta e calcula informações trabalhistas
from datetime import date
dic={}
dic['Nome']=input('Digite o nome: ').capitalize()
dic['Sexo']=input('Digite o Sexo [F/M]: ').upper()
while dic['Sexo']!='F' and dic['Sexo']!='M':
        print('Digite uma opção valida!')
        dic['Sexo']=input('Digite o Sexo [F/M]: ').upper()
dic['Idade']=(date.today().year) - int(input('Digite o ano de nascimento: '))
dic['CTPS']=input('Digite o número da CTPS: ')
if dic['CTPS']!='0':
    dic['Contratação']=int(input('Digite o ano de contratação: '))
    dic['Salário']=('R$',input('Digite o salário: R$'))
    if dic['Sexo']=='M':
        dic['Aposentadoria']=(40-(date.today().year - dic['Contratação']))+date.today().year
    else:
        dic['Aposentadoria']=(35-(date.today().year - dic['Contratação']))+date.today().year
print('\033[33m{:>20}\033[m'.format('Informações'))
for k, v in dic.items():
    print(f'{k}: {v}')

