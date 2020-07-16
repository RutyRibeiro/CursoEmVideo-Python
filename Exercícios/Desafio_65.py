
soma=0
quant=0
esc='S'
maior=0
menor=0
cont=0
while esc!='N':
    num=int(input('Digite um número: '))
    soma=soma+num
    quant+=1
    if cont==0:
        maior=num
        menor=num
        cont+=1
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    esc=(input('Deseja continuar? [S/N]')).upper()
    # while esc!='S' or esc!='N':
    #     print("Digite uma opção válida!")    
    #     esc=(input('Deseja continuar? [S/N]')).upper()
    #     if esc=='S' or esc=='N':
    #         break
print('A média entre os números é: {}\nMaior: {}\nMenor: {}'.format(soma/quant,maior,menor))
