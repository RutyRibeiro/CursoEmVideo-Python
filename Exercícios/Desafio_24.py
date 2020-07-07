#Recebe nome de cidade e analisa se começa com Santo
cid=input(print('Digite o nome da cidade: '))
cid=cid.upper()
if (cid.find('SANTO')) == 0:
    print('Nome da cidade começa com Santo!' )
else:
    print('Nome da cidade não começa com Santo!')