# recebe nome e media, adiciona a um dicionario junto com a situação mostrando o conteudo no final
dic={}
dic['Nome']=input('Digite o nome do aluno: ').capitalize()
dic['Média']=float(input(f'Digite a média de {dic["Nome"]}: '))
if dic['Media']>=7:
    dic['Situação']='Aprovado'
else:
    dic['Situação']='Reprovado'
for k,v in dic.items():
    print(f'{k}: {v}.')

