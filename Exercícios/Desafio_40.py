#lê duas notas e mostra a situação do aluno
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
print('\033[34mMédia\033[m: {}'.format(media))
if media<5:
    print('\033[32mSituação: \033[mAluno reprovado!')
elif media>= 5 and media <7:
    print('\033[32mSituação: \033[mAluno em recuperação!')
else:
    print('\033[32mSituação: \033[mAluno aprovado!')

