# programa com função para apresentação de frases formatadas 

# função que adapta a apresentação da frase proposta
def escreva(frase):
    tam=len(frase)+4
    print('-' * tam)
    print(f'  {frase}  ')
    print('-' * tam)


# programa principal
escreva('Olá, mundo!')
escreva('Curso em Vídeo')