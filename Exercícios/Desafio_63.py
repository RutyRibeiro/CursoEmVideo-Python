# mostra sequencia de Fibonacci de acordo com a quantidade do numero digitado
print('\033[33mSequência de Fibonacci!\033[m')
num=int(input('Digite a quantidade de números: '))
i=0
vet=[]
while i<num:
    if i==0: 
        vet.append(0)
    elif i==1:
        vet.append(1)
    else:
        vet.append(vet[i-1]+vet[i-2])
    i+=1
print(vet)
          