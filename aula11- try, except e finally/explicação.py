# print(10/0) - ZerroDivisorError

# lista = [0 , 1, 2, 3] - IndexError
# print(lista[4]) - IndexError

# dicionario = {"chave" : "valor"} - KeyError
# print(dicionario["victor"]) - KeyErro

try :
    num1 = 18
    num2 = 5

    num3 = num1/ num2

    print(num3)

    listabacana = [num3]
    print(listabacana[0])

    #Raise - chama um erro para acontecer
    raise ZeroDivisionError

except ZeroDivisionError as erro:
    print("Não posso dividir por 0")
    print(f"Erro: {erro}")

except ZeroDivisionError as erro:
    print("Não existe esse elemento na linha")
    print(f"Erro: {erro}")

except KeyError as erro :
    print("A chave não existe")
    print(f"Erro: {erro}")

except Exception :
    print("Ocorreu um erro desconhecido")
    print(f"Error desconhecido:")

finally :
    print("Este bloco é sempre executado")

    # TRY - TENTA RODAR O CÓDIGO
    # EXCEPT - CASO DE UM ERRO ESPECÍFICO
    # FINALLY - ÚLTIMO CÓDIGO A SER EXECUTADO
    # Atenção: Ao usar o finally, ele sempre será executado, independentemente se houve ou não um erro
    # O finally é usado para fechar recursos ou limpar memória
   