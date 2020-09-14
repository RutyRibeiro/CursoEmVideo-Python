# programa com função que gera ficha de jpgador em um campeonato 
def ficha(nome, gols):
    """
    ->gera ficha de um jogador em um campeonato 
    param.(nome):nome do jogador 
    param.(gols): numero de gols do jogadorno campeonato             
    return: 
    """
    if nome=='':
        nome="<desconhecido>"
    if gols=='':
        gols=0
    print (f'O jogador {nome} fez {gols} gol(s) no campeonato')


# programa principal
ficha(input('Digite o nome do jogador: ').capitalize(),input('Digite a quantidade de gols do jogador: '))