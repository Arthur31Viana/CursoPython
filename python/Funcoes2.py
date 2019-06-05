#Criar função que calcula vários números
def calcula_dobro(numero):
    total = numero * 2
    return total

def calcula_soma_numeros(*numeros): #O argumento passa a ser uma lista
    return sum(numeros)

def calcula_soma_numeros(**numeros): #O argumento passa a ter chave e valor
    return sum(numeros)
import pdb;pdb.set_trace() #Break point

def calcula_soma_numeros(**numeros):
    return sum(numeros.values())



#Chamar função
resultado = calcula_dobro(10)
print(resultado)

soma = calcula_soma_numeros(2,3,4)
print("O resultado da soma é %d" % soma)

soma = calcula_soma_numeros(num1=5, num2=10, num3=20)
print("O resultado da soma é %d" % soma)
