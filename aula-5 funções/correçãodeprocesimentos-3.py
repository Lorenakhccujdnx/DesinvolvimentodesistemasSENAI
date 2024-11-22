# 3) faça um algoritmo que leia três notas
#  de um aluno, calcule e escreva 
# a média final deste aluno. 
# Considerar que a média é ponderada 
# e que o peso das notas é 2,3 e 5.

notas = [0,0,0]


for i in range (0,3,1):
    nota = float(input(f"Digite a {i+1}º nota:"))
    notas[i] = nota

mediaFinal = (notas[0] *2 + notas [1] *3 + [2] *5)/ 10
#
print(f"A media final do aluno é :")