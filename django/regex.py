import re

#Retorna a confirmação das letras que tem na string
#a = re.match('Py', 'Python') #Procura qualquer coisa que comece com Py na segunda string
#a = re.match('[pP]y]', 'Python') #Procura qualquer coisa que comece com py/Py na segunda string
#a = re.match('[a-zA-Z]y', 'Python') #Procura qualquer coisa que comece de a-zy/A-Zy na segunda string

#Retorna em forma de lista todas as ocorrências listadas na string
#a = re.findall('[a-zA-Z]y', 'Python jython') #Procura qualquer coisa que comece de a-zy/A-Zy na segunda string
#a = re.findall('[a-zA-Z][a-zA-Z]', 'Python jython') #Procura qualquer coisa de duas letras que comece de a-z/A-Z na segunda string
#a = re.findall('[a-zA-Z][a-zA-Z]+', 'Python jython') #Procura qualquer coisa de duas letras que comece de a-z/A-Z e tenha qualquer tamanho na segunda string
#a = re.findall('\w+', 'Python jython') #Inclui números

#Fromas de print buscando as strings
#print(a)
#print(re.search(r'teste[a-z]{2}$', 'testes')) #Busca em testes a palavra teste com caracteres de a-z e tenha mais dois carcteres

end = 'www.site.com/clientes/1'
#print(re.search(r'clientes/\d+$', end)) #Procurar em end se tem cliente/     #\d+$ representa números de qualquer tamanho
#Extrae o id do cliente e mostra em forma de lista
print(re.split(r'clientes/(?P<id>\d+)', end)) #Procurar em end se tem cliente/  #(?P<id>\d+) representa parametro agrupado
#print(re.split(r'(clientes)/(?P<id>\d+)', end)) #Retorna o que o cliente é
