# Calcula aumento de salario de acordo com a faixa de valores
sal = float(input('Digite o salário:'))
if sal > 1250.00:
    print('Novo salário: {}'.format(sal + (10 / 100) * sal))
else:
    print('Novo salário: {}'.format(sal + (15 / 100) * sal))
