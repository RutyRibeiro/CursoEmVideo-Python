#lê numero, calcula fatorial
num=int(input('Digite um número: '))
cont=num
fat=1
while cont>0:
    fat=fat*cont
    cont-=1
print('{}! = {}'.format(num,fat))