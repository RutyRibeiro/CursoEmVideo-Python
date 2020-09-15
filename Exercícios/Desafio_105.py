# programa com função que retorna dicionário a partir de notas paasadas como parametros
def notas(*notas,sit=''):
    dic={}
    dic['Quantidadede notas:'] = len(notas)
    dic['Maior nota:'] = max(notas)
    dic['Menor nota:'] = min(notas)
    dic['Media:'] =sum(notas)/len(notas)
    if sit==True:
        if dic['Media:']<5:
            dic['Situação:']='Ruim'
        else:
            dic['Situação:']='Boa'
    return dic

# Programa principal
resul=notas(4.5,4,6.9, sit=True)
print(resul)
