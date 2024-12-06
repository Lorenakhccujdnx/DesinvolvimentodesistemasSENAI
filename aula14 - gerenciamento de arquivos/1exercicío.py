# Crie um arquivo onde você possa escolher entre fazer cadastro ou login,
#  faça o cadastro salvar as informações em um json e no login que ele realmente verifique se esse usuario existe

import json 
usuario ={
    "nome" : "Lorena",
    "senha" : "1771",
    "email" : "lorena@gmail.com"

}

with open('usuarios.json', 'w') as file:
    json.dump(usuario, file, indent=4)
    print("Usuário cadastrado com sucesso!")



def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    with open('usuarios.json', 'r') as file:
        usuarios = json.load(file)
        for user in usuarios:
            if user['email'] == email and user['senha'] == senha:
                print("Login efetuado com sucesso!")
                return True
            
            

