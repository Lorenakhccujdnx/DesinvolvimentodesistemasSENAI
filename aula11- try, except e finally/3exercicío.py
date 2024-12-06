# 4)Crie um programa que simule um caixa eletrônico. 
# Peça ao usuário um valor a ser sacado e deduza de um saldo inicial.
#  Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada.
#  Garanta que o saldo atualizado seja sempre exibido no finally.

saldo = 50 

while True:
        try:
                opcao = int(input("1 - SACAR \n2 SALDO \n0 - SAIR \n"))

                match opcao:
                        case 1:
                                try :
                                        valorSaque = float(input("Quanto deseja sacar? \n"))

                                        if valorSaque > saldo :
                                                raise Exception
                                        elif valorSaque < 0 :
                                                raise Exception
                                        else:
                                                print (f"O valor R$ {valorSaque} foi sacado")
                                                saldo -= valorSaque
                                except Exception :
                                        print ("OPERAÇÃO INVÁLIDA")
                        case 2:
                                print(f"SALDO DISPONÍVEL É DE R$ {saldo}")         
                        # sim e não \n - pular para próxima linha

                        case 0:
                                confirma = input("Confirma? s/n \n").lower ()

                                if confirma == "s":
                                        break
                                else:
                                        continue
                        case _:
                                print ("Opção inválida, tente novamente!")
                 
        except ValueError as erro:
                print(f"Opção inválida, tente novamente! Código do erro {erro}")

        except Exception as erro:
                print(f"Erro desconhecido, tente novamente! Código do erro {erro}")
        finally:
                print (f"Usuário, saldo disponível é de R$: {saldo}")
# MATCH - VAI SER BASICAMENTE O IF E ELSE . VAI ACESSAR O CASO 1....        