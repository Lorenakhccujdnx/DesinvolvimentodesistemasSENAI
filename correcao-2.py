def parImpar (numero):

    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
print(parImpar(7))
print(parImpar(2))
#  Quando se usa 'return', coloca para imprimir e depois a 
# variavel 'print(parImpar())