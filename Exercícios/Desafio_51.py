# le primeiro termo e razao de pa, mostra os 10 primeiros termos usando laço for
print('\033[36mCalculo de PA!\033[m')
razao=int(input('Digite a Razão:'))
pt=int(input('Digite o Primeiro Termo: '))
print('Os 10 primeiros termos da PA:')
for i in range(0,10):
    print('{}° termo: {}'.format(i+1, pt+i*razao))