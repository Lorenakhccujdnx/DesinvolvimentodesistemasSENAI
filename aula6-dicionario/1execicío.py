#1. Cadastro de Produto
# Você precisa criar um programa que armazene informações de um produto em um dicionário. 
# As informações devem incluir nome, preço e quantidade em estoque. 
# Depois, o programa deve exibir todas as informações do produto.


# Dicionário para armazenar as informações do produto

def cadastrar_produto():
    produto = {}
    produto['nome'] = input("Digite o nome do produto: ")
    produto['preço'] = float(input("Digite o preço do produto: "))
    produto['quantidade'] = int(input("Digite a quantidade em estoque: "))

    return produto

def exibir_produto(produto):
    print("\nInformações do produto:")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preço']:.2f}")
    print(f"Quantidade em estoque: {produto['quantidade']}")

# Cadastro do produto
produto = cadastrar_produto()

# Exibindo as informações do produto
exibir_produto(produto)
