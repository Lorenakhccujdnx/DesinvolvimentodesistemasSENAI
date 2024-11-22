lista = [1,2,3,4,6,8]
print(lista, type(lista))
lista.append(10)
print(lista)

# tupla - não mutavél
cordenada_x = "-999"
cordenada_y = "-888"
localizacao = (cordenada_x, cordenada_y)

# se colocar as chaves {} o código vira uma tupla altomaticamente  
localizacao.append("")
# colocar código correto nos parênteses
print(localizacao, type(localizacao))