def lim(list, lim):
    quant = 0
    for elem in list:
        if elem > lim:
            quant+=1
    return quant

quant = lim([4,4],3) 
print(quant)