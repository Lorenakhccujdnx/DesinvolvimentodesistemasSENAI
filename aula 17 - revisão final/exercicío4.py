# 4)Crie uma classe Aluno que tenha os atributos nome, notas (uma lista)
#  e métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). 
# Todo aluno criado deverá ser adicionado a um Json

# etapas :
# 1 - criar o aluno (objeto), precisa ter nome e notas
# 2 - método do aluno calcular a média
# 3 - verificar quem foi aprovado ou não
# 4 - calcular a média, criar objetos
# 5 - verificar se existe alunos anteriores
# 6 - exportar para um json
# self - sempre será característica do objeto

import json
import os

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    # método do aluno calcular a média
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    # verificar quem foi aprovado ou não
    def verificar_aprovado(self):
        return self.calcular_media() >= 7
    
    def exportar_aluno(self):
        dados_alunos = {
            "nome": self.nome,
            "notas": self.notas,
            "media": self.calcular_media(),
            "aprovado": self.verificar_aprovado()
        }
        # se o arquivo existe! Se sim salva em dados
        # se não dados vazio []
        if os.path.exists("dados.json"):
            with open("dados.json", "r", encoding="utf8") as arquivo:
                dados = json.load(arquivo)
        else:
            dados = []
        dados.append(dados_alunos)
        with open("dados.json", "w", encoding="utf8") as arquivo:
            json.dump(dados, arquivo, indent=4)

# criando objetos

aluno1 = Aluno("Victor", [8, 5, 9, 7])
aluno2 = Aluno("Lorena", [10, 9, 8, 9])

# verificando média e aprovado

print(f"Média de {aluno1.nome}: {aluno1.calcular_media()}")
print(f"{aluno1.nome} foi aprovado: {aluno1.verificar_aprovado()}")

print(f"Média de {aluno2.nome}: {aluno2.calcular_media()}")
print(f"{aluno2.nome} foi aprovado: {aluno2.verificar_aprovado()}")

# exportando para um json

aluno1.exportar_aluno()
aluno2.exportar_aluno()

# verificando se os dados foram salvos

with open("dados.json", "r", encoding="utf8") as arquivo:
    dados = json.load(arquivo)

print(dados)

