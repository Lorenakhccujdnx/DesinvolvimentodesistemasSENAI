def somarMuitos(*numeros) :
    valorTotal = 0

    for numero in numeros:
        valorTotal += numero
        print(numeros, valorTotal)

somarMuitos (1,2)
somarMuitos (250,901,412,312)
somarMuitos (410,1203)

# código diferente
# sum - somar
print(sum([1,5,7,8,9]))