# modulo com algumas funções para cálculo monetário
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