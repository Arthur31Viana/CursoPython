a = [1, 2, 3]

a.append(4) #Insere o valor no final da lista
a.clear() #Limpa a lista
b = a.copy() #Tira copia da lista para o b
a.extend(b) #Junta os valores das duas listas
a.insert(3, 'Novo valor') #Insere um novo valor na posição desejada
a.pop() #Remove o ultimo item da lista e retorna o valor
a.remove('Novo valor') #Remove por completo o valor desejado
a.reverse() #Inverte o valor dentro da lista
a.sort() #Ordena a lista