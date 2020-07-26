# recebe valores pra uma lista mostra a quantidade de elementos digitados, elementos em dorma decrescente e se o numero 5 faz parte desta lista
esc='S'
lista=[]
while esc=='S':    
    lista.append(int(input('Digite um número: ')))
    esc=(input('Deseja continuar [S/N]:')).upper()
    while esc!='S' and esc!='N':
        print('Digite uma opção valida!')
        esc=(input('Deseja continuar [S/N]:')).upper()
    print('\n')
lista.sort(reverse=True)
print('O tamanho da lista é: {}\nLista descrescente: {}'.format(len(lista),lista))
if 5 in lista:
    print('O número 5 está na lista! ')
else:
    print('O número não 5 está na lista! ') 