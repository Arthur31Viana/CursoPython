i = 0 #Contador

while i<10:
    if i == 5:
        break #Para o loop quando chegar em 5
        i += 1
        continue #Pula o número
    print(i)
    i += 1 #Variável recebe + 1
else:
    print('Fim do loop')
