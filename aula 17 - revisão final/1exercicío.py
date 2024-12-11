"""
1) Implemente um sistema de gerenciamento de estoque que inclua classes Produto,
 Estoque e métodos para adicionar, remover e verificar produtos.
 
 a) Crie uma classe Produto com nome, preço e quantidade em estoque.
  b) Crie uma classe Estoque que tenha uma lista de Produtos e métodos para adicionar, remover e verificar produtos.
  c) Implemente métodos para adicionar, remover e verificar produtos do estoque.
  d) Crie um objeto do Estoque e teste os métodos para adicionar, remover e verificar produtos.
  """

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = []


    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'O produto {produto.nome} foi adicionado ao estoque.')

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f'O produto {nome_produto} foi removido do estoque.')
                return
        print(f'O produto {nome_produto} não foi encontrado no estoque.')


    def verificar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                print(f'O produto {produto.nome} possui {produto.quantidade} unidades em estoque.')
                return
        print(f'O produto {nome_produto} não foi encontrado no estoque.')

# Testando o sistema

estoque = Estoque()

produto1 = Produto('Leite', 2.50, 100)
produto2 = Produto('Arroz', 3.50, 50)
produto3 = Produto('Feijão', 4.00, 75)

estoque.adicionar_produto(produto1)

estoque.adicionar_produto(produto2)

estoque.adicionar_produto(produto3)

estoque.verificar_produto('Leite')

estoque.remover_produto('Arroz')

estoque.verificar_produto('Arroz')

estoque.verificar_produto('Feijão')




