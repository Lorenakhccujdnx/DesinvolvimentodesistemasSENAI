# UPER 
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saldo = 0
        self.avaliacao = 5

    def adicionarSaldo(self,valor):
            #self é usado quando não se sabe o valor do código
        self.saldo += valor
        print(f"O valor de {valor} foi adicionado")

cliente = Cliente("Victor",21)
cliente.adicionarSaldo(100)
print(cliente.saldo, cliente.avaliacao)

