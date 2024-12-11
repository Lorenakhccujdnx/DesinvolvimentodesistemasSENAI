"""""""""""""""
2. Agenda de Contatos
 Crie um programa para armazenar números de telefone. 
 O usuário deve poder adicionar novos contatos (nome como chave e número como valor).
  Depois, o programa deve exibir todos os contatos cadastrados.
  Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"
"""""""""
def adicionar_contato(agenda):
    while True:
        nome = input("Digite o nome do contato (ou 'finalizar' para encerrar): ")
        if nome.lower() == 'finalizar':
            break
        numero = input("Digite o número de telefone: ")
        agenda[nome] = numero

def exibir_contatos(agenda):
    print("\nContatos cadastrados:")
    for nome, numero in agenda.items():
        print(f"Nome: {nome}, Telefone: {numero}")

# Programa principal
def main():
    agenda = {}
    adicionar_contato(agenda)
    exibir_contatos(agenda)

if __name__ == "__main__":
    main()

