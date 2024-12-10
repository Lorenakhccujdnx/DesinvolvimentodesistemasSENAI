# Maior e menor 
#a)Crie um programa que solicite ao usuário que insira 4 números.
#b)Identifique e imprima o maior e o menor número da lista inserida


# Importando a função max() e min() do Python

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
num4 = float(input('Digite o quarto número: '))

maior = max(num1, num2, num3, num4)

menor = min(num1, num2, num3, num4)

print(f'O maior número é: {maior}')

print(f'O menor número é: {menor}')
