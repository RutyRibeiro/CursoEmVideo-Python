# programa com função que só recebe númeos inteiros
def leiaInt(num):
    while True:
        # testa se a string é numerica caso True transforma em um int
        if num.isnumeric():
            num=int(num)
        # testa se é um numero inteiro 
        if isinstance(num,int):
            return num
        else:
            print('Digite um valor válido!')
            num=input('Digite um número inteiro: ')

# programa principal
num=leiaInt(input('Digite um número inteiro: '))
print(f'Você digitou o número: {num}')   