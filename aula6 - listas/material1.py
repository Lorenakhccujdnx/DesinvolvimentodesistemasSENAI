alunosPt1 = ["Carlos", "Alessandra", "Geraldo"]
alunosPt2 = ["Guilerme", "Paloma", "Natan"]

alunosPt3 = alunosPt1 + alunosPt2
print (alunosPt3)

alunosPt1.extend(alunosPt2)
print (alunosPt2)

# for + array
print (len(alunosPt1))

# para que contador print todos os nomes de alunosPt1
for nome in alunosPt1:
    print (f"- {nome} \n ###")
# as # vãom ser usadas como texto    