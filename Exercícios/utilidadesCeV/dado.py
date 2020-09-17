
def substituir(num):
    if num.find(',') != -1:
        num=num.replace(',','.')
    return num

def teste (num):
    try:
        float(num)
    except ValueError:
        return False
    return True

def leiafloat(num):
    while True:
        num=substituir(num)
        testando=teste(num)

        if testando==True:
            num=float(num)
            return num
        else:
            print('Digite um valor válido!')
            num=input('Digite o preço: ')

           
    