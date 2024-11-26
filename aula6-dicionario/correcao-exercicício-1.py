#1. Cadastro de Produto
# Você precisa criar um programa que armazene informações de um produto em um dicionário. 
# As informações devem incluir nome, preço e quantidade em estoque. 
# Depois, o programa deve exibir todas as informações do produto.
# Obs : O salvamento devrá parar apenas quando o usuário digitar "finalizar".

agenda = {}

while True:
    nome = input("Digite o nome do usuario: ")

    if nome == "finalizar":
        break

    telefone = input(f"Digite o numero de telefone da(o) {nome}: ")
    print("finalizar")

    agenda.update({
        nome : telefone
    })

print("----AGENDA ELETRÔNICA----")
for contato in agenda.items():
    print(f"Nome : {contato[0]} - Telefone {contato[1]}" )