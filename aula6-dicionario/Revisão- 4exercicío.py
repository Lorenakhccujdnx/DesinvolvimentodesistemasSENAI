# 4)Implemente uma lojinha virtual simples! 
# Onde possamos ter um catálogo com 5 produtos 
# e nesse podemos adicionar ao carrinho ou visualizar-lo.
#  Até chegarmos na finalização do qual mostrará o valor total

def mostrar_catalogo(produtos):
    print("Catálogo de Produtos:")
    for codigo, produto in produtos.items():
        print(f"{codigo}: {produto['nome']} - R$ {produto['preço']:.2f}")

def adicionar_ao_carrinho(carrinho, produtos):
    codigo = input("Digite o código do produto que deseja adicionar ao carrinho: ")
    if codigo in produtos:
        if codigo in carrinho:
            carrinho[codigo]['quantidade'] += 1
        else:
            carrinho[codigo] = {
                'nome': produtos[codigo]['nome'],
                'preço': produtos[codigo]['preço'],
                'quantidade': 1
            }
        print(f"{produtos[codigo]['nome']} adicionado ao carrinho.")
    else:
        print("Código de produto inválido.")

def visualizar_carrinho(carrinho):
    if carrinho:
        print("Carrinho de Compras:")
        for item in carrinho.values():
            print(f"{item['nome']} - R$ {item['preço']:.2f} x {item['quantidade']}")
    else:
        print("Carrinho está vazio.")

def finalizar_compra(carrinho):
    total = sum(item['preço'] * item['quantidade'] for item in carrinho.values())
    print(f"Valor total da compra: R$ {total:.2f}")

def main():
    produtos = {
        '1': {'nome': 'Camiseta', 'preço': 50.00},
        '2': {'nome': 'Calça', 'preço': 100.00},
        '3': {'nome': 'Tênis', 'preço': 200.00},
        '4': {'nome': 'Boné', 'preço': 30.00},
        '5': {'nome': 'Jaqueta', 'preço': 150.00}
    }
    
    carrinho = {}

    while True:
        print("\n1. Mostrar Catálogo")
        print("2. Adicionar ao Carrinho")
        print("3. Visualizar Carrinho")
        print("4. Finalizar Compra")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            mostrar_catalogo(produtos)
        elif opcao == '2':
            adicionar_ao_carrinho(carrinho, produtos)
        elif opcao == '3':
            visualizar_carrinho(carrinho)
        elif opcao == '4':
            finalizar_compra(carrinho)
            break
        elif opcao == '5':
            print("Saindo da lojinha virtual.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
