"""
1) Crie um programa onde consiga verificar se uma pessoa é maior de idade, 
caso sim, informe "maior de idade", caso não, "menor de idade"
"""

idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
