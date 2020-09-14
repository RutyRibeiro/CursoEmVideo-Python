# programa com função que determina a situação de voto a partir do ano de nascimento 
from datetime import date

def voto(ano):
    """
    ->determina a situacao de voto de uma pessoa
    param.(ano):ano de nascimento
    return: se esta ou nao apto ao voto
    """
    idade=date.today().year - ano
    if idade>65 or (idade>=16 and idade<18):
        resul=f' Com {idade} anos: Voto é opcional!'
    elif idade<16:
        resul=f' Com {idade} anos: Voto não é permitido!'
    else:
        resul=f' Com {idade} anos: Voto é obrigatório!'
    return resul


# programa principal
anoNasc=int(input('Digite o ano de nascimento: '))
resul=voto(anoNasc)
print(f'{resul}')