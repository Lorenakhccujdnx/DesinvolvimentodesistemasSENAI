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
# 
# Verifica se o arquivo existe, caso não, cria um novo

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._notas = []
# (UMA UNDERLINE) = PROTECTED (NÃO PODE SER ALTERADO FORA DA CLASSE)
    def adicionar_notas(self, notas):
        self._notas.append(notas)
    def calcularMedia(self):
        if self._notas:
            return sum(self._notas) / len(self._notas)
        # sum - somar tudo que está na lista
        # len - quantidade de itens na lista
        # \ - dividir 
        else: 
            return 0
        
    def verificarAprovacao(self) :
        media = self.calcularMedia()
        if media >= 7:
               print(f"Aluno(a) {self.nome} foi aprovado com média: {media}")
        else:
            print(f"Aluno(a){self.nome} não foi aprovado")

    def exportarAluno(self):
        dados_alunos = {
            "nome": self.nome,
            "notas": self._notas,
            "media": self.calcularMedia(),
            "aprovacao": self.verificarAprovacao()
        }
        # se o arquivo existe! Se sim salva em dados
        # se não dados vazio []
        if os.path.exits("dados.json"):
            with open("dados.json", "r", encoding="utf8") as arquivo:
                # r - ler
                try :
                     dados = json.load(arquivo)
                except json.JSONDecodeError:
                     dados = []
              
        else :
            dados = []
        
        dados.append(dados_alunos)

        with open("dados.json", "w", encoding="utf8") as arquivo:
         # w - escrever
            json.dump(dados, arquivo, indent=2)

Aluno1 = Aluno("Victor")
Aluno1.adicionar_notas(8)
Aluno1.adicionar_notas(5)
print(Aluno1._notas)
Aluno1.verificarAprovacao()

Aluno2 = Aluno("Bruna")
Aluno2.verificarAprovacao()

Aluno3 = Aluno("Pedro")
Aluno3.adicionar_notas(5)
Aluno3.adicionar_notas(6)
Aluno3.verificarAprovacao()

Aluno1.exportarAluno()
Aluno2.exportarAluno()
Aluno3.exportarAluno()

# print(aluno2.__dict__)
# vars - vai abrir objeto