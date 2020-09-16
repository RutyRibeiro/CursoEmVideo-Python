# modulo com algumas funções para cálculo monetário
def moeda(quant):
    retorno = (f'R${quant:.2f}')
    return retorno

def aumentar(quant,p):
    retorno = float(quant+(p/100*quant))
    return retorno

def diminuir(quant,p):
    retorno = float(quant-(p/100*quant))
    return retorno

def dobro(quant):
    retorno =  float(quant*2)
    return retorno

def metade(quant):
    retorno = float(quant/2)
    return retorno