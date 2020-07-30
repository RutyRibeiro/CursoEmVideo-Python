# recebe nome e media, adiciona a um dicionario junto com a situação mostrando o conteudo no final
dic={}
dic['nome']=input('Digite o nome do aluno: ').capitalize()
dic['media']=float(input(f'Digite a média de {dic["nome"]}: '))
if dic['media']>5:
    dic['situacao']='Aprovado'
else:
    dic['situacao']='Reprovado'
for k,v in dic.items():
    print(f'a {k} é {v} !')

