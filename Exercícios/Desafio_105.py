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
        elif 5<=dic['Media:']<=7:
            dic['Situação:']='Razoável'
        else:
            dic['Situação:']='Boa'
    return dic

# Programa principal
resul=notas(2,2,2, sit=False)
print(resul)
