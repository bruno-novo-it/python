class Transporte():

    def __init__(self, nome, peso, preco):
        self.nome =  nome
        self.peso = peso
        self.preco = preco
    
    def GetNome(self):
        return self.nome
    
    def GetPeso(self):
        return self.peso
    
    def GetPreco(self):
        return self.preco

class Carro(Transporte):

    def __init__(self, nome, peso, preco, preco_seguro):
        Transporte.__init__(self, nome, peso, preco)
        self.preco_seguro = preco_seguro
    
    def GetPrecoSeguro(self):
        return self.preco_seguro
    

#t = Transporte("Fusca", 500, 3278.3)

#print(t.GetNome())

#print(t.GetPreco())

carro = Carro("Fusca", 300.78, 3500.00, 800.00)

print("Nome do Carro: {}".format(carro.GetNome()))
print("Peso do Carro: {} Kg".format(carro.GetPeso()))
print("Valor do Carro: {} reais".format(carro.GetPreco()))
print("Valor do Seguro: {} reais".format(carro.GetPrecoSeguro()))