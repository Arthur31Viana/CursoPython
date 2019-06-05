for i in range(10): #Contagem do 0 ao 10
    print(i)
else:
    print('Fim loop')

list1 = ['Maçã', 'Banana', 'Melão']
list2 = ['Tomate', 'Cebola', 'Cenoura']

for i, j in zip(list1, list2):
    print(i, j)

for i, j in enumerate(list1): #Enumera a lista
    print(i, j)