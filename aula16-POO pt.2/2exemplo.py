
"""
RELAÇÕES ENTRE CLASSES
ASSOCIAÇÃO - RELACIONA UM OBJETO A OUTRO
"""
class Usuario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login
        self._senha = senha
        self.livro = None
    # PROPERTY CHAMANDO OBJETO EXTERNO E RETORNANDO
    # "PEGO O OBJETO E RETORNO"
    @property
    def livroAdd(self):
        return self.livro
    # PEGA O QUE FOI RETORNADO E ACRESCENTA NO ATRIBUTO
    # "PEGO O QUE FOI RETORNADO E ACRESCENTO NO USUARIO"
    @livroAdd.setter
    def livroAdd(self, livroAdd):
        self.livro = livroAdd
class Livro:
    def __init__(self,nome,autor):
       self.nome = nome
       self.autor = autor
    def mostrarAutor(self):
        return self.autor 
user = Usuario('Victor','083983','senha')
book = Livro('1984','George Orwell')
user.livro = book
print(user.livro.mostrarAutor())
# USER
#  LIVRO
#   MOSTRARAUTOR
print(f'USER:{user.__dict__}\nLIVRO:{book.__dict__}')
print(f'{user.livro}')