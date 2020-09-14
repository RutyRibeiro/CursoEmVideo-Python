# programa com funcao para calcular fatorial 
def fatorial(n,show=''):
    """
    ->calcula o fatorial de um numero
    param.(n):número a ser calculado o fatorial 
    param.(show): caso seja true mostrará o processo do calculo             
    return: fat -> resultado do calculo
    """
    fat=1
    for i in range(1,n+1):
        if show:
            print(f' {i} x', end='') if i!=n else  print(f' {i} = ', end='')
        fat=fat*i
    return fat,i

# função principal
num=fatorial(5,True)
print(num)

        

            
