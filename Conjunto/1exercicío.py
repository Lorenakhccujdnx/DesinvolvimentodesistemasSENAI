"""
1)Encontrar alunos que cursam apenas uma disciplina dado as disciplinas:
-matematica com os nomes dos alunos que fazem Matemática
-fisica com os nomes dos alunos que fazem Física

Encontre os alunos que fazem apenas uma das disciplinas.
"""

matematica = ['Ana', 'Pedro', 'João']
fisica = ['João', 'Carlos', 'Mariana']

# Encontrar alunos que fazem apenas Matemática ou apenas Física

apenas_uma_disciplina = (set(matematica) - set(fisica)).union(set(fisica) - set(matematica))

print('Alunos que fazem apenas uma disciplina:', list(apenas_uma_disciplina))
