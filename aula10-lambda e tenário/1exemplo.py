def converteDolar(valor):
    valor *= 5.82
    return valor

print (converteDolar(5))

# def nome(parametro)
#    processo
#vs
#lambda parametro : processo
converterEuro = lambda valor : valor * 6.66
print(converterEuro(20))

# VANTAGEM DO LAMBDA :
# LAMBDA É UMA FUNÇÃO ANÔNIMA
# RESUME PROCESSOS SIMPLES
# AJUDA LEGIBILIDADE
# EVITA CHAMAR UM DEF EM CASO DE UMA LINHA

# DESVANTAGENS :
# NÃO É EFICAZ EM PROCESSOS MAIORES
# EM FALTA DE ATENÇAÕ, DIFICULTA VARIÁVEIS
converterEuro = lambda valor : valor * 6.6
converterIene = lambda valor, taxa : valor / 0.03 - taxa
print (converterEuro(20))
print(converterIene(1000,40))

# TERNARIO
condicao = True
if condicao :
    print("IF")
else :
    print("ELSE")

print("IF") if condicao else print ("ELSE")
# TERNÁRIO É UMA ESTRUTURA DE SELEÇÃO SIMPLES
# SE FOR TRUE VAI IMPRIMIR IF, SE FOR FALSE VAI IMPRIMIR ELSE
valor = 0
valor = 1 if condicao else valor
print(valor)