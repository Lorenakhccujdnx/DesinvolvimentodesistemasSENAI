"""
3)ler 3 números Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos
"""
maior = 0

for i in range (0,3,1) :
    numero = int(input(f"Digite o {i + 1} número:"))

    if numero > maior :
        maior = numero

print(f"O maior número é: {maior}")