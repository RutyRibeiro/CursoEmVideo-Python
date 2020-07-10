#le primeiro termo e razao de pa, mostra os 10 primeiros termos, após isso mostra apenas a quantidade de termos recebidos 
print('\033[36mCálculo de PA!\033[m')

razao=int(input('Digite a Razão:'))
pt=int(input('Digite o Primeiro Termo: '))

print('Os 10 primeiros termos da PA:')
i=0
while i<10:
    print('{}° termo: {}'.format(i+1, pt+i*razao))
    i+=1
esc=int(input('Deseja mostrar mais quantos termos? '))
while esc!=0:
    for i in range(i,i+esc):
        print('{}° termo: {}'.format(i+1, pt+i*razao))
    esc=int(input('Deseja mostrar mais quantos termos? '))
    i+=1
