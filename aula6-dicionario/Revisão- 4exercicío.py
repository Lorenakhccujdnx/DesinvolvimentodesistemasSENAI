# 4)Implemente uma lojinha virtual simples! 
# Onde possamos ter um catálogo com 5 produtos 
# e nesse podemos adicionar ao carrinho ou visualizar-lo.
#  Até chegarmos na finalização do qual mostrará o valor total

print("1- R$ 3.00 toddynho")
print("1- R$ 3.50 coxinha")
print("1- R$ 2.70 suco de uva")
print("1- R$ 6.00 biscoito de goiabada")
print("1- R$ 8.90 rafaello")
print("1- R$ 5.00 pastel de fango com catupiry")

carrinho = []

while True:
    produto = input("Escolha um produto (0 para sair): ")
    if produto == "0":
        break
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    carrinho.append((quantidade, preco))