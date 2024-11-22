valorTotal = 0
def somarValor(valorProduto):
    global valorTotal
    
   # valorProduto = float(input("Preco do produto"))
    valorTotal += valorProduto

# argumento - valor entre parênteses
somarValor(30)
somarValor(5)
somarValor(47)

print(f"valor total é de R$:{valorTotal}")
