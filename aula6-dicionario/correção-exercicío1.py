#1. Cadastro de Produto
# Você precisa criar um programa que armazene informações de um produto em um dicionário.
# As informações devem incluir nome, preço e quantidade em estoque.
# Depois, o programa deve exibir todas as informações do produto.

produtos = {
    "Nomes" : ["Pastel", "Leite"],
    "Preco" : [7.50, 4.99],
    "Quantidade" : [7, 10]
}

nome = input("Nome do produto :")
produtos.get("Nomes").append("Nome")
preco = float(input("Preco do produto :"))
produtos.get("Preco").append("Preco")
quantidade = int(input("Quantidade em estoque :")) 
produtos.get("Quantidade").append("Quantidade")

# intruduzir se e se nao if : else:

for produto in produtos.items():
    print(f"{produto[0]}")
    print(f"{produto[1]}")