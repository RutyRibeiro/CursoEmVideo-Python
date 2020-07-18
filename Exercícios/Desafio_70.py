# lê nome e preco dos produtos de uma compra termina quando recebe n como resposta  no final mostra informações 
esc='S'
total=0
contPreco=0
nomeMenor=''
precoMenor=0
cont=0
while esc!='N':
    produto=input('\nDigite o nome do produto: ')
    preco=float(input('Digite o preço do produto: R$'))
    total=total+preco
    if preco>1000:
        contPreco+=1
    if cont==0:
        precoMenor=preco
        nomeMenor=produto
        cont+=1
    else:
        if preco<precoMenor:
            precoMenor=preco       
            nomeMenor=produto
    esc=(input('Deseja continuar? [S/N]: ')).upper()
    if esc!='S' and esc!='N': 
        while esc!='S' and esc!='N':
            print("Digite uma opção válida!")    
            esc=(input('Deseja continuar? [S/N]: ')).upper()
print(f'\nPreço total da compra: {total:.2f}\nQuantidade de produtos com o preço acima de R$1000,00: {contPreco}\nNome do produto mais barato: {nomeMenor} eu custa R${precoMenor}')
       