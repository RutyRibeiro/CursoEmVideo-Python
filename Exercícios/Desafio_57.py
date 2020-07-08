#Lê sexo de uma pessoa mas só aceita f e m
sexo=''
cont=0
while sexo!='F' and sexo!='M':
    if cont>=1:
        print('Digite uma opção válida!')
    sexo=(input('Digite o sexo [F/M]: ')).upper()
    cont+=1
if sexo == 'F':    
    print('Pessoa do sexo Feminino')
else:
    print('Pessoa do sexo Masculino')
    