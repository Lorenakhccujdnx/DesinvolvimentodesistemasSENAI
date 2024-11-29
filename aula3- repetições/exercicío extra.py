tentar = "s"
nome_cadastrado = "ADM"
senha_cadastrada = "ADM"

while tentar == "s":
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    if nome_cadastrado == nome and senha_cadastrada == senha:
       print(f"Seja bem vindo(a), {nome}")
       break
    else : 
        print("Nome ou senha incorretos! Tente novamente!")