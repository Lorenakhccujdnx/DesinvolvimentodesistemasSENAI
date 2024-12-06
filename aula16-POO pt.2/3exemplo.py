
"""
AGREGAÇÃO - "FORMA MAIS ESPECIALIZADA DE ASSOCIAÇÃO"
"""
class Carrinho:
    def __init__(self):
        self.produtos = []
    def inserirProduto(self,*produtos):
        for p in produtos:
            self.produtos.append(p)
    
    def listarProdutos(self):
        for produto in self.produtos:
            print(produto.nome)
            print(produto.preco)
class Produto:
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco
carrinho = Carrinho()
p1 = Produto('Relogio do Ben 10',350)
p2 = Produto('Hotwheels',10)
carrinho.inserirProduto(p1,p2)
carrinho.listarProdutos()
print(carrinho.__dict__)