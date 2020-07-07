# Aprova ou não um emprestimo bancario baseado no tempo e salario do comprador
sal=float(input('Digite o salário do comprador: R$'))
tempo=int(input('Digite o periodo de pagamento em anos: '))
val=float(input('Digite o valor do imóvel: R$'))

prestação= val/(tempo*12)

print('prestação: R${:.2f} por mês\nPeriodo: {} anos'.format(prestação,tempo))

if prestação < (30/100)*sal:
    print('\033[32mSituação: \033[mEmpréstimo aceito!')
else:
    print('\033[32mSituação: \033[mEmpréstimo negado, ultrapassa 30% do salário do comprador!')
