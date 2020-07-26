# cadastra 5 números em ordem crescente diretamentre em uma lista
lista=[]
for i in range (0,5):
    op=0
    num=int(input('Digite um número: '))
    for i in range(0,len(lista)):
        if op==1:
            break
        if num<=lista[i]:
            lista.insert(i,num)
            op+=1
    if op==0:
        lista.append(num)
print('Os números digitados em ordem crescente são: {}'.format(lista))