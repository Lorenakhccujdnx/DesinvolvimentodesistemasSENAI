#1) Crie uma função que multiplica todos os argumentos
#  não nomeados recebidos e Retorne o total para uma variável
#  e mostre o valor da variável.

def operacao(*numeros):
    resultado = 1

    for numero in numeros:
        resultado *= numero
    print (f"O valor da operacao foi de:{resultado}")

# Testando a função

operacao(30, 5, 47)