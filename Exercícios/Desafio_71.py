# caixa eletronico, recebe valor a ser devolvido e calcula quais notas serão devolvidas
quant=float(input('Digite o valor a ser sacado: R$'))
cont=quant
cem=0
cinq=0
vinte=0
dez=0
cinco=0
dois=0
um=0
while cont-100>=0:
    cont=cont-100
    cem+=1
while cont-50>=0:
    cont=cont-50
    cinq+=1
while cont-20>=0:
    cont=cont-20
    vinte+=1
while cont-10>=0:
    cont=cont-10
    dez+=1
while cont-5>=0:
    cont=cont-5
    cinco+=1
while cont-2>=0:
    cont=cont-2
    dois+=1
while cont-1>=0:
    cont=cont-1
    um+=1
print(f'\nIMPRIMINDO R${quant:.2f}\n') 
if cem !=0 :
    print(f'Notas de R$100,00: {cem}')
if cinq !=0 :
    print(f'Notas de R$50,00: {cinq}')
if vinte !=0 :
    print(f'Notas de R$20,00: {vinte}')
if dez !=0 :
    print(f'Notas de R$10,00: {dez}')
if cinco !=0 :
    print(f'Notas de R$5,00: {cinco}')
if dois !=0 :
    print(f'Notas de R$2,00: {dois}')
if um !=0 :
    print(f'Notas de R$1,00: {um}')