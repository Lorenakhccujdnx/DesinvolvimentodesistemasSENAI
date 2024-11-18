# Manipulação de listas
# Crie uma lista com os números `[5, 8, 2, 9, 1]`.
# Ordene a lista em ordem crescente e depois em ordem decrescente.
# Adicione o número `7` ao final da lista e depois insira o número `3` na posição 2.
# Substitua o valor na posição 1 por `10` e remova o valor `9` da lista.
# Exclua os elementos da posição 2 até a posição 4.

lista1 = [5,8,2,9,1]
print(lista1)

# Ordenando a lista em ordem crescente
#sort é uma função padrão pra ordenar os algaritmos de forma crescente
lista1.sort()
print(f"Ordenada em ordem crescente: {lista1}")
# Também poderá ser print(lista1) 

# Ordenando a lista em ordem decrescente
# reverse=True - vai reverter a função de sort e torná-lo descrescente
lista1.sort(reverse=True)
print(f"Ordenada em ordem decrescente: {lista1}")

# Adicionando o número 7 ao final da lista

lista1.append(7)
print(f"Adicionado 7: {lista1}")

# Inserindo o número 3 na posição 2

lista1.insert(2,3)
print(lista1)

# Substituindo o valor na posição 1 por 10

lista1[1] = 10
print(f"Substituir o valor na posição 1 por 10: {lista1}")

# Removendo o valor 9 da lista

lista1.remove(9)
print(f"Remover o valor 9: {lista1}")

# Excluindo os elementos da posição 2 até a posição 4 

del lista1[2:5]
print(f"Excluindo elementos da posição 2 até a posição 4: {lista1}")


