# 98 POP
# nome_motorista1 = "Geraldo"
# carro_motorista1 = "Renault Kwid"

#class - "molde do objeto"
# def _init_() - função contrutora
# self - "O próprio objeto"
# PascalCase - primeira letra de todas as palavras maiúsculas (Cliente,Carro)
# obs : CamelCase - Sempre começa com maiúsculo (clienteVip)

class Motorista:
    def _init_(self,nome,carro,corCarro,placa):
        self.nome = nome
        self.carro = carro
        self.corCarro = corCarro
        self.placa = placa


motorista1 = Motorista("Geraldo","Renault Kwid","Rosa pink","1234-top")
motorista2 = Motorista("Victor","Camaro","Preto supreme","777-top")
motorista1.nome = "Geraldo"
motorista1.nome = "Geraldo"
motorista1.carro = "Renault Kwid"
print(motorista1.carro)

print(motorista1, type(motorista1))