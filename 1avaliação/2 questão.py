# 2)Escreva um programa para um sistema de controle de estoque de uma loja. 
# O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos 
# e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:

# dicas :
# Adicionar um novo produto ao estoque.
# Atualizar a quantidade de um produto existente.
# Verificar se um produto está disponível (quantidade maior que 0).
# Continuar exibindo o menu até que o usuário escolha sair.

def mostrar_menu():
    print("1. Adicionar um novo produto ao estoque")
    print("2. Atualizar a quantidade de um produto existente")
    print("3. Verificar se um produto está disponível")
    print("4. Sair")

def adicionar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    if nome_produto in estoque:
        estoque[nome_produto] += quantidade
    else:
        estoque[nome_produto] = quantidade
    print(f"{nome_produto} adicionado com sucesso!")

def atualizar_quantidade(estoque):
    nome_produto = input("Digite o nome do produto: ")
    if nome_produto in estoque:
        quantidade = int(input("Digite a nova quantidade: "))
        estoque[nome_produto] = quantidade
        print(f"A quantidade de {nome_produto} foi atualizada para {quantidade}.")
    else:
        print(f"{nome_produto} não encontrado no estoque.")

def verificar_disponibilidade(estoque):
    nome_produto = input("Digite o nome do produto: ")
    if nome_produto in estoque and estoque[nome_produto] > 0:
        print(f"{nome_produto} está disponível com {estoque[nome_produto]} unidades.")
    else:
        print(f"{nome_produto} produto fora de estoque.")

def main():
    estoque = {}
    while True:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_produto(estoque)
        elif opcao == 2:
            atualizar_quantidade(estoque)
        elif opcao == 3:
            verificar_disponibilidade(estoque)
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
