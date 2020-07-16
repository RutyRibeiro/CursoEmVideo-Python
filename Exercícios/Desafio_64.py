# lê numeros termina quando recebe 999 
num=0
st=''
nume=0
while num!='999':
    num=input('Digite um número: ')
    if num!='999':    
        st=st+' '+num
        nume+=1
print('Foram digitados: {} números\nSão eles: {}'.format(nume,st))
