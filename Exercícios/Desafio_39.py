# analisa alistamento de acordo com o ano de nascimento digitado
from datetime import date
nasc = int (input('Digite o ano de nascimento: '))
sexo = input('Digite o Sexo (F/M): ')
sexo = sexo.upper()

if sexo == 'M':
    idade = (date.today().year) - nasc
    if idade <18:
        print('\033[32mIdade\033[m: {}\n\033[32mSituação\033[m: Ainda vai se alistar ao serviço militar'.format(idade))
        print('Tempo até o periodo de alistamento: {}'.format(18-idade))
    elif idade == 18:
        print('\033[32mIdade\033[m: {}\n\033[32mSituação\033[m: Está na hora de se alistar!'.format(idade))
    else:
        print('\033[32mIdade\033[m: {}\n\033[32mSituação\033[m: Passou da hora de se alistar'.format(idade))
        print('Tempo até de atraso de alistamento: {} anos'.format(idade-18))
elif sexo == 'F':
    print('Independente da idade mulheres não são obrigadas a se alistarem!')
else:
    print('Digite o sexo corretamente!')