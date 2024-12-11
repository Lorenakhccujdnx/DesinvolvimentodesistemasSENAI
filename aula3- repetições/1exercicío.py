"""
1) Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).
"""

num_tabuada = int(input("Qual tabuada deseja :"))

i = 0
while i <= 10 :
    print(f"{i} x {num_tabuada} = {i * num_tabuada}")
    i += 1