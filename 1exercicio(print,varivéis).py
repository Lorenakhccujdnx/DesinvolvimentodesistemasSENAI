# 1) Escreva um algoritmo que leia nome, email e senha de usuário
#  e mostre após o cadastro com os dados salvos.

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = {
        "Nome": nome,
        "Email": email,
        "Senha": senha
    }

    print("\nDados cadastrados com sucesso:")
    print(f"Nome: {usuario['Nome']}")
    print(f"Email: {usuario['Email']}")
    print(f"Senha: {usuario['Senha']}")

# Chamando a função para cadastrar o usuário
cadastrar_usuario()


