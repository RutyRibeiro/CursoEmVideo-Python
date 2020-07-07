# lê 3 números e analisa qual o maior e o menor
num1=int(input('Digite o 1° numero'))
num2=int(input('Digite o 2° numero'))
num3=int(input('Digite o 3° numero'))
maior=num1
menor=num1
# Calcula maior
if num1>num2 and num1>num3:
    maior=num1
else:
    if num2>num1 and num2>num3:
        maior=num2
    else:
        maior=num3
# Calcula menor
if num1<num2 and num1<num3:
    menor=num1
else:
    if num2<num1 and num2<num3:
        menor=num2
    else:
        menor=num3

print('maior: {}\nMenor: {}'.format(maior,menor))