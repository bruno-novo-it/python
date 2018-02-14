# Aula 15 - Encapsulemento de Dados
  # Acessando váriáveis privados
  # Deixando o código mais elegante

class Pessoa:

    def __init__(self):
        self.__nome = None
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

p = Pessoa() # Instância sem nenhum atributo definido

p.nome = "Bianca"

print(p.nome)