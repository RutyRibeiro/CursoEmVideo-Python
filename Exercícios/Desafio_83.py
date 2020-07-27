# analisa se a expressão recebida tem parenteses dispostos corretamente
exp=input('Digite sua expressão: ')
exp=list(exp)
# resolução usando loop:
# abre=0
# fecha=0
# for v in exp:
#     if v=='(':
#         abre+=1
#     if v==')':
#         fecha+=1
abre=exp.count('(')
fecha=exp.count(')')
if abre == fecha:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')