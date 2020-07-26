# recebe números aleatorios caso o número seja unico é cadstrado em uma lista, no final mostra números cadastrados em ordem crescente
lista=[]
i='S'
while i=='S':
    num=int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        i=(input('Deseja continuar [S/N]:')).upper()
        while i!='S' and i!='N':
            print('Digite uma opção valida!')
            i=(input('Deseja continuar [S/N]:')).upper()
    else:
        print('Valor já cadastrado, tente novamente!')
    print('\n')
print ('Números cadastrados em ordem crescente: {}'.format(sorted(lista)))