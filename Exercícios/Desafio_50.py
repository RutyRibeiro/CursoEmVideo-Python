# lê 6 numero diferentes e faz a soma apenas dos numeros pares
soma=0
st=''
for i in range(0,6):
    num=int(input('Digite o {}° número: '.format(i+1)))
    if num%2==0:
        soma=soma+num
        st=('{} {}'.format(st,num))
print('A soma dos numeros pares({}) é: {}'.format(st,soma))