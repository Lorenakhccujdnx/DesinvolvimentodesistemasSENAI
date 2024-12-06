# Windows - cls
# macOs e Linux - clear


class Motorista :
    def __init__(self,nome):
        self.nome = nome  
    # Atributo da classe Motorista
        self.carro = None

    def associarCarro(self,carro):
        self.carro = carro
        print(f" O motorista {Motorista.nome} está associado ao carro!")
class Carro:
    def __init__(self,nome):
        self.nome = nome 
        self.velocidade = 0
        self.portaMalas = ['Step']
    def acelerar(self,velocidadeAcelerada):
    # os.system("csl")
    # para limpar terminal
        if velocidadeAcelerada <= 0:
            print("VALOR INVÁLIDO!")
        else :
            self.velocidade += velocidadeAcelerada
            print(f"Acelerei: {velocidadeAcelerada} \n")
            print (f"Velocidade atual: {self.velocidade}")
    # += acréscimo

    def adicionarPortaMalas(self, *items):
        print("Porta malas do carro")
    # *items - permite passar uma quantidade indefinida de argumentos
        for item in items:
            self.portaMalas.append(item)
            
        for numero, item in enumerate(self.portaMalas):
            print(f'{numero+1} - {item}')
        # {numero+1} -para que não comece a contar do 0
        # mas pode ser colocado só o {numero}

Motorista = Motorista ("Victor")
c1 = Carro("Lamborguini")
# carro pode ser = c1

Motorista.associarCarro(c1) 
Motorista.carro.acelerar(100)
Motorista.carro.acelerar(50)
Motorista.carro.adicionarPortaMalas("Compras", "Mala", "Cooler")

print(f"Motorista.__dict__")
print(vars(c1))
