esc='S'
while esc=='S':
    num=int(input('Digite um valor: '))
    if num not in lista:
        
        i=(input('Deseja continuar [S/N]:')).upper()
        while i!='S' and i!='N':
            print('Digite uma opção valida!')
            i=(input('Deseja continuar [S/N]:')).upper()
    else:
        print('Valor já cadastrado, tente novamente!')
    print('\n')