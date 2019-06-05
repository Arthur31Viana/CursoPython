#Herda tudo o que está em object
class Casa(object):

    # Atributo + valores
    cor = 'Vermelha'
    altura = 3
    quartos = 10

    # Construtor
    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    def imprime_casa(self):
        print(self.cor, self.altura, self.quartos)

    # Método
    def pintar(self, cor):
      self.cor = cor

    def diminui_quarto(self, quartos):
        self.quartos = quartos


#Chamando Construtor
minha_casa = Casa('Azul', 5, 3)
minha_casa.imprime_casa()

#Chamando função
minha_casa = Casa()
print(minha_casa.cor, minha_casa.altura, minha_casa.quartos)

#Chmando método
minha_casa.pintar('Roxa')
print(minha_casa.cor)

minha_casa.diminui_quarto(2)
print(minha_casa.quartos)

#Chamando construtor
minha_casa = Casa('Azul', 5, 3)
print(minha_casa.cor, minha_casa.altura, minha_casa.quartos)