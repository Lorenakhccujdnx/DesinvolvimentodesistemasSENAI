try :
    num1 = int(input("Digite primeiro número: "))
    operador = input ("Digite o operador: ")
    num2 = int(input("Digite o segundo número: "))

    resultado = 0
    match operador :
        case '+' :
            resultado = num1 + num2
        case '-' :
            resultado = num1 - num2
        case '*' :
            resultado = num1 * num2
        case '/' :
             resultado = num1 / num2

except ValueError :
    print("VALOR INVÁLIDO")
except ZeroDivisionError :
    print("NÃO POSSO DIVIDIR UM NÚMERO POR 0")
except Exception :
    print("OPERAÇÃO INVÁLIDA")
finally:
    print(f"Resultado final é de: {resultado}")