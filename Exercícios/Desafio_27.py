# recebe nome e mostra o primeiro e ultimo nome
nome=input(print('Digite o nome'))
nome=nome.split()
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome[1],nome[len(nome)-1]))