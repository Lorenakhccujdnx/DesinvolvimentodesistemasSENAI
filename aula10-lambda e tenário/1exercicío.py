"""
1) Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).
"""
def tabuada_8():
    numero = 8
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')

tabuada_8()
