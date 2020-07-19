# recebe um número e o escreve por extenso 
numeros=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
num=int(input('Digite um número entre 0 e 20: '))
while num>20 or num<0:   
    print('Digite um número válido!')
    num=int(input('Digite um número entre 0 e 20: '))
print(f'SEU NÚMERO: {num} = {numeros[num]}')