import json

def loginUsuario():
    while True:
        login = input("Digite a sua senha:")
        senha = input("Digite sua senha novamente:")

        with open('dados.json', 'r', encoding= "utf8") as leitura:
            dados = json.load(leitura)
            c_login = dados ["login"]
            c_senha = dados ["senha"]
            c_nome = dados ["nome"]

        if c_login == login and c_senha == senha:
            print(f"Seja bem vindo(a), {c_nome}")
            break
        else :
            print("Usuário ou senha incorretos!")