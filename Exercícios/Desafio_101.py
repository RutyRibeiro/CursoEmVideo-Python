# programa com função que determina a situação de voto a partir do ano de nascimento 
from datetime import date

def voto(ano):
    global idade
    idade=date.today().year - ano
    if idade>65 or (idade>=16 and idade<18):
        resul='Voto opcional!'
    elif idade<16:
        resul='Não vota!'
    else:
        resul='voto obrigatório!'
    return resul


# programa principal
idade=int(input('Digite o ano de nascimento: '))
resul=voto(idade)
print(f'Com {idade} anos: {resul} ')