import json


def cadastrarUsuario():
    nome = input ("Digite o nome:")
    login = input ("Digite seu login (email):")
    cpf = int(input("Digite seu cpf (7777777):"))

    dados = {
        "nome" : nome,
        "login" : login,
        "cpf" : cpf,
        "senha" : senha
    }
    while True:
        senha = input ("Digite sua senha:")
        c_senha = input ("Digite a sua senha novamente:")

    # c_senha - é de confirme a sua senha

        if senha == c_senha:
          break
        else:
           print ("Senhas não conferem. Tente novamente.")

    with open("dados.json", "w", encoding= "utf8") as leitura :
        json.dump(
            dados,
            leitura,
            indent = 2
        )
        