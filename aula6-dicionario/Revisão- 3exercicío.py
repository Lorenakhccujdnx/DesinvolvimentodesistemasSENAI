# 3)Crie um programa que permita ao usuário adicionar tarefas
#  a uma lista, marcar como concluídas ou remover tarefas

# Inicialmente, crie uma lista vazia para armazenar as tarefas

tarefas = []

# Defina as funções para adicionar, marcar como concluída
#  e remover tarefas

def adicionar_tarefa(nova_tarefa):
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada.")

def marcar_concluida(tarefa_index):
    if 0 <= tarefa_index < len(tarefas):
        tarefa = tarefas[tarefa_index]
        tarefas[tarefa_index] = f"[Concluída] {tarefa}"
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        print("Tarefa não encontrada.")
        

