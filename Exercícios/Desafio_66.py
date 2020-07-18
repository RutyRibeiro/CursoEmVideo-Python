# lê numeros, para quando digitado 999 no final mostra quantidade do numeros digitados e a soma entre eles
num=0
soma=0
quant=0
while num!=999:
    num=int(input('Digite um número: '))
    if num==999:
        break
    soma=soma+num
    quant=quant+1
print(f'Foram digitados {quant} números e a soma entre eles é: {soma}')
    