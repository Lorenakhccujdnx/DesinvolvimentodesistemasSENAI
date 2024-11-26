# 3)Crie um programa que permita ao usuário adicionar tarefas
#  a uma lista, marcar como concluídas ou remover tarefas

# Inicialmente, crie uma lista vazia para armazenar as tarefas

tarefas = []

while True: 
    print("tarefas")
    for tarefa in tarefas:
        print = (f"- {tarefas}")


    print = ("*****")
    print = ("A- Adicionar tarefa")
    print = ("B- Remover tarefa")
    print = ("C- Marcar tarefa como concluída")
    escolha = input("Digite o que quer executar:")

    match escolha :
        case "a" :
          tarefa = input("Qual tarefa deseja adicionar: ")
          tarefas.append(tarefa)  

        case "b" :
            tarefa = input("Qual tarefa deseja remover: ")
            tarefas.remove(tarefa)

        case "c" :
            break
        case _:
         print("Opção inválida. Tente novamente.")

    