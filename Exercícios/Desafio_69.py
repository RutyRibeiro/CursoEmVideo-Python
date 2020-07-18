# le sexo e idade, termina quando digitado 'n' no final mostra informações
contmaior=0
contmu=0
homens=0
idade=0
sexo=''
esc='S'
while esc!='N':
    sexo=(input('\nDigite o sexo [F/M]: ')).upper()
    if sexo!='F' and sexo!='M': 
        while sexo!='F' and sexo!='M':
            print("Digite uma opção válida!")    
            sexo=(input('Digite o sexo [F/M]: ')).upper()
    idade=int(input('Digite a idade: '))
    if idade>18:
        contmaior+=1
    if sexo=='M':
        homens+=1
    if sexo=='F' and idade<20:
        contmu+=1
    esc=(input('Deseja continuar? [S/N]: ')).upper()
    if esc!='S' and esc!='N': 
        while esc!='S' and esc!='N':
            print("Digite uma opção válida!")    
            esc=(input('Deseja continuar? [S/N]: ')).upper()
print(f'\nQuantidade de pessoas maiores de 18 anos: {contmaior}\nQuantidade de homens cadastrados: {homens}\nQuantidade de mulheres com menos de 20 anos: {contmu}')
       