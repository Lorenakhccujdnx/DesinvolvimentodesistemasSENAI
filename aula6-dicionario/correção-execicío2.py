"""""""""""""""
2. Agenda de Contatos
 Crie um programa para armazenar números de telefone. 
 O usuário deve poder adicionar novos contatos (nome como chave e número como valor).
  Depois, o programa deve exibir todos os contatos cadastrados.
  Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"
"""""""""""

contatos = {}

def adicionar_contatos():
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o número do contato: ")