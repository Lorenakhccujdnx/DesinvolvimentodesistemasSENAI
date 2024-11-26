# 4)Implemente uma lojinha virtual simples! 
# Onde possamos ter um catálogo com 5 produtos 
# e nesse podemos adicionar ao carrinho ou visualizar-lo.
#  Até chegarmos na finalização do qual mostrará o valor total 

# entrada - lista de produtos
# processo -  somar valores
# saída - mostrar o valor total 

escolha = None
carrinho = []
valorTotal = 0

def carregarCatalogo():
    print("1- R$ 3.00 toddynho")
    print("2- R$ 3.50 coxinha")
    print("3- R$ 2.70 suco de uva")
    print("4- R$ 6.00 biscoito de goiabada")
    print("5- R$ 8.90 rafaello")
    print("6- R$ 5.00 pastel de fango com catupiry")
    print("7- MOSTRAR CARRINHO")
    print("8- FINALIZAR")

    global escolha
    escolha = input("Digite a opção desejada:")

def adicionarCarrinho (nome, valor):
     carrinho.append("nome")
     global valorTotal
     valorTotal += valor
     print(f"{nome} Item adicionado ao carrinho!") 

while True:
# o catálogo vai ficar em loop    
    carregarCatalogo()

    if escolha == "1" :
        carrinho.append("Toddynho", 3.00)
    elif escolha == "2":
        adicionarCarrinho("Coxinha", 3.50)
    elif escolha == "3":
        adicionarCarrinho("Suco de uva", 2.70)
    elif escolha == "4":
        adicionarCarrinho("Biscoito de goiabada", 6.00)
    elif escolha == "5":
        adicionarCarrinho("Rafaello", 8.90)
    elif escolha == "6":
        adicionarCarrinho("Pastel de frango com catupiry", 5.00)
    elif escolha == "7":
        print("MOSTRAR CARRINHO")
    elif escolha == "8":
        print("FINALIZAR")
        break
          
    else :
        print("Opção inválida! Tente novamente!")
print(f"O valor da compra foi de: {valorTotal}") 
# if e else só roda se for um em baixo do outro