#Recebe dois números gera menu com opções de operações entre eles
opcao=9
num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
while opcao!='5':
    opcao=input('\n\033[33m[01]\033[m Somar\n\033[33m[02]\033[m Multiplicar\n\033[33m[03]\033[m Maior\n\033[33m[04]\033[m Novos números\n\033[33m[05]\033[m Sair\n\nDigite uma opção: ')
    print('') 
    if opcao =='1':
        print('{} + {} = {}'.format(num1,num2, num1+num2))
    elif opcao =='2':
        print('{} X {} = {}'.format(num1,num2, num1*num2))
    elif opcao=='3':
        if num1>num2:
            print('Maior: {}\nMenor: {}'.format(num1,num2))
        else:
            print('Maior: {}\nMenor: {}'.format(num2,num1))
    elif opcao=='4':
        num1=int(input('Digite o primeiro número: '))
        num2=int(input('Digite o segundo número: '))
    else:
        if opcao!='5':
            print('\nDigite uma opção válida!\n')
print('\033[34mFim!\033[m')
    