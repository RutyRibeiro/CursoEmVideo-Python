#determina quais são todas as vogais das palavras pré-determinadas em uma tupla
tupla=('APRENDER','PROGRAMAR','ESTUDAR','PRATICAR','TRABALHAR')
for i in range(0,len(tupla)):
    palavra=list(tupla[i].lower())
    vogais=''
    for j in range(0,len(palavra)):
        if palavra[j]=='a' or palavra[j]=='e' or palavra[j]=='i' or palavra[j]=='o' or palavra[j]=='u':
            vogais = vogais +' '+ palavra[j]
    print('Vogais da palavra {} são:{}'.format(tupla[i],vogais))

    