"""
1) Escreva um algoritmo que verifique o usuario e senha 
(considere por padrão o usuario cadastrado : "nome = ADM", "senha = ADM"), 
caso o usuário informe a senha ou nome incorretos. Repita as perguntas para que ele tente novamente,
caso acerte, imprima a mensagem "bem vindo ADM" e finalize a aplicação
"""

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