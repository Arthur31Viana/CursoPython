d = {key: value, key: value, key: value,} #Definição de um dicionário

d = {'nome': 'Fulano', 'idade': 18, 'Salario': 5000,}
print(d)

d.setdefault() #Tentar achar o valor, se não achar ele add ao dicionario
d.popitem() #Remove o primeiro elemento e retorna
d.get() #Retorna o elemento, se não tiver, dá erro
d.fromkeys() #As chaves recebendo o mesmo elemento
