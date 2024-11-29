""""
SETS - CONJUNTOS 

1 - NÃO TEM ÍNDICE
2 - NÃO ACEITA CONTEÚDO DUPLICADOS
3 - É CONSTRUIDO COM {} ou set()

# SET É UM CONJUNTO QUE QUEBRA O 
# STRING EM VÁRIOS CARACTERES DIFERENTES
# SET - NÃO ACEITA CONJUNTO REPETIDO 
# EX : a  = set("LORENA","LORENA","LORENA")
# print(a)

# DICIONARIO E SETS SÃO BEM SEMELHANTES
# TIRANDO A DIFERENÇA DAS CHABES QUE É USADA EM SETS
"""""

# CRIANDO SET

a  = set("LORENA")
print(a)


b = {"Lorena", 1,2,3,4,5,6}
print(b)

c = set()
print(c, type (c))

# MÉTODOS UTÉIS
conjunto = set()
conjunto.add(10)
conjunto.add(7)

conjunto.update((12, 15, 17))
# É PRECISO ADICIONAR MAIS UM () 
# PARA GERAR MAIS DE UM NÚMERO DE UMA SÓ VEZ

print ("*" * 7)
print(conjunto)
# VAI MULTIPLICAR OS * DE ACORDO COM O NÚMERO COLOCADO

conjunto.remove(12)
conjunto.discard(15)

# remove - remove um elemento do conjunto
# discard - discarta um elemento do conjunto

# UNIÃO (union) - PEGAR OS DOIS DIAGRAMAIS E UNIR
# INTERSECÇÃO (intersection) - É O QUE TEM EM COMUM NOS DOIS
# DIFERENÇA  (difference) - QUANDO O ITEM ESTÁ PRESENTE APENAS EM UM CONJUNTO

conjuntoA = {1,2,3,4,5,6,7}
conjuntoB = {7,6,5,4,3,2,1}
conjuntoC = set()

# | UNION
conjuntoC.update(conjuntoA.union(conjuntoB))
conjuntoC = conjuntoA | conjuntoB
 # OS DOIS TEMA MESMA FUNÇÃO

# & INTERSECTION
conjuntoC = conjuntoA & conjuntoB
# difference = diferença em relação ao conjunto da esquerda
conjunto = conjuntoB - conjuntoA
# ^ DIFFERENCE = DIFERENÇA EM RELAÇÃO A AMBOS OS CONJUNTOS

conjuntoC = conjuntoA ^ conjuntoB

for elemento in conjuntoC :
    print(elemento)
    
print(conjuntoC)