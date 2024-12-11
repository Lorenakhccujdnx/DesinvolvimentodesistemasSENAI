# 4)Crie duas classes:
# 1 Autor, com os atributos:  Nome, nacionalidade e livros
# 2 Livro, com os atributos: titulo, ano e autor
# Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
# Imprima o nome do autor e a lista dos seus livros.

# Etapas:
 # 1 - Criar as classes Autor e Livro
 # 2 - Criar um objeto Autor e dois objetos Livro
 # 3 - Associar os livros ao autor
 # 4 - Imprimir o nome do autor e a lista dos seus livros
 # self - sempre será característica do objeto
 # __init__ - método construtor da classe
class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return f"Autor: {self.nome}, Nacionalidade: {self.nacionalidade}, Livros: {[livro.titulo for livro in self.livros]}"

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo}, Ano: {self.ano}, Autor: {self.autor.nome}"

# Criação do autor
autor1 = Autor("Machado de Assis", "Brasileiro")

# Criação dos livros
livro1 = Livro("Dom Casmurro", 1899, autor1)
livro2 = Livro("Como eu era antes de você", 2012, autor1)

# Adicionando os livros ao autor
autor1.adicionar_livro(livro1)
autor1.adicionar_livro(livro2)

# Imprimindo o nome do autor e a lista dos seus livros
print(autor1)




