# modulo com funções uteis para cálculo monetário
def moeda(quant):
    retorno = (f'R${quant:.2f}')
    return retorno

def aumentar(quant,p,form=''):
    retorno = float(quant+(p/100*quant))
    if form==True:
        retorno=moeda(retorno)
    return retorno

def diminuir(quant,p,form=''):
    retorno = float(quant-(p/100*quant))
    if form==True:
        retorno=moeda(retorno)
    return retorno

def dobro(quant,form=''):
    retorno =  float(quant*2)
    if form==True:
        retorno=moeda(retorno)
    return retorno

def metade(quant,form=''):
    retorno = float(quant/2)
    if form==True:
        retorno=moeda(retorno)
    return retorno

def resumo(quant, porAu, porDim):
    print('{:^70}'.format('RESUMO DO VALOR'))
    print('{:-^70}'.format('-'))
    print('{:.<60} {:>7}'.format('Preço analisado:',moeda(quant)))
    print('{:.<60} {:>7}'.format('Dobro do preço:',dobro(quant,True)))
    print('{:.<60} {:>7}'.format('Metade do preço:',metade(quant,True)))
    print('{:.<60} {:>7}'.format(f'{porAu}% de aumento:',aumentar(quant,porAu,True)))
    print('{:.<60} {:>7}'.format(f'{porDim}% de redução:',diminuir(quant,porDim,True)))
    print('{:-^70}'.format('-'))