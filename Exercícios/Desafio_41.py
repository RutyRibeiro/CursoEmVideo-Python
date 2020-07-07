# le ano de nascimento do atleta e define categoria de acordo com a idade
from datetime import date
nasc = int (input('Digite o ano de nascimento: '))
idade = (date.today().year) - nasc
if idade <=9:
    print('\033[34mCategoria\033[m: Mirim')
elif idade<=14:
    print('\033[34mCategoria\033[m: Infantil')
elif idade<=19:
    print('\033[34mCategoria\033[m: Junior')
elif idade<=20:
    print('\033[34mCategoria\033[m: Sênior')
else:
    print('\033[34mCategoria\033[m: Master')

