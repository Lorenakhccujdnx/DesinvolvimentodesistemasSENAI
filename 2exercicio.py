# 2 - faça um algoritmo para calcular a idade da pessoa baseado no ano do seu nascimento 
# calculate_age - calcular_idade
# current-year - ano_atual

def calcular_idade(idade):
    ano_atual = 2024
    return ano_atual - idade
 
# 3 - utilize a função para calcular a idade do aluno

nascimento_aluno = 1995
idade_aluno = calcular_idade(nascimento_aluno)
print(f"A idade do aluno é {idade_aluno} anos.")


