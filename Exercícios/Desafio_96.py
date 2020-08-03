# programa cria função basica para calcular area de terreno

# Função para calcular area
def area(larg,compr):
    area=larg*compr
    print(f'A area do terreno {larg} X {compr} equivale a {area} metros quadrados')


# programa principal
print('\033[33mCalcula área\033[m')
area(float(input('Digite o comprimento em metros: ')),float(input('Digite a largura em metros: ')))
