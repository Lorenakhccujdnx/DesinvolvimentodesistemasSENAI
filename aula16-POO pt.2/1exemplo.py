
""" 
ENCAPSULAMENTO
(SEM UNDERLINE) = PUBLIC (PODE SER ALTERADO DURANTE TODO O CÓDIGO)
(UMA UNDERLINE) = PROTECTED (NÃO PODE SER ALTERADO FORA DA CLASSE)
(DOIS UNDERLINES) = PRIVATE (NÃO É ACESSADO POR OUTRAS PARTES DO CÓDIGO)
"""
# defina a classe:
class Carro:
    def __init__(self,nome,cor,placa,peso,marca):
        self.__nome = nome
    # não pode ser alterado (privado)
        self.cor = cor
    # pode ser alterado durante todo o código
        self._placa = placa
    # só podemos alterar dentro da classe
        self.peso = peso
        self.marca = marca
        self.km_atual = 0
    
    def alterarPlaca(self,placa):
        self.placa = placa
        print(f'Alterei a placa para {self.placa}')
carro1 = Carro('Fiat Uno','Branco','FIATOP',20,'Fiat')
print(carro1)
# dois metodos para apresentar objeto
print(vars(carro1))
carro1.alterarPlaca('ESCADAGOD')
# imprime a placa alterada da placa
print(carro1.__dict__)
# imprime todo