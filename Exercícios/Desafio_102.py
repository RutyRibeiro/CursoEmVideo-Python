def fatorial(n,show=''):
    fat=1
    for i in range(1,n+1):
        if show:
            print(f' {i} X', end='') if i!=n else  print(f' {i} =')
        fat=fat*i
    return fat

num=fatorial(5,True)

        

            
