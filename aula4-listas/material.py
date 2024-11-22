"""""""""
LISTAS
"""""""""

# cliente1 = "Vitor"
# cliente2 = "Alan"
# cliente3 = "Bruna"

# CRUD - CREATE (CRIAR), READ (LER), UPDATE (ATUALIZAR), DELETE (APAGAR)

# clientes = ["Vitor", "Alan", "Bruna"]
# teste = ["texto",123, True,[]]
# clientesAlt = list()

# print(type (clientes))
# print(teste)

# METODOS DE UMA LISTA
lista = ["Copo","Banana","Kit Kat","Bebida"]
print(lista)

# APPEND - PARA ACRESCENTAR ALGO AO FINAL DA LISTA 
lista = ["Copo","Banana","Kit Kat","Bebida"]
lista.append("VideoGame")
print(lista)

lista = ["Copo","Banana","Kit Kat","Bebida", "VideoGame"]
lista.insert(4, "Suco")
print(lista)

del lista[1]
print(lista)
# indíce 0 1 2  3 4 / -4 -3 -2 -1 Começa a contar do 0, logo banana é 1 
#print(lista[1])
# lista.clear ()- Deletar tudo da lista