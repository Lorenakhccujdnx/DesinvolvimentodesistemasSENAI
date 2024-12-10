# 5)Implemente uma função chamada calculadora que: Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).
# Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json

import json

def calculadora(num1, num2, operacao):
    historico = []
    resultado = None
    
    if operacao == 'adição':
        resultado = num1 + num2
    elif operacao == 'subtração':
        resultado = num1 - num2
    elif operacao == 'multiplicação':
        resultado = num1 * num2
    elif operacao == 'divisão':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    else:
        resultado = "Operação inválida."
    
    historico.append({
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    })
    
    with open('historico.json', 'w') as file:
        json.dump(historico, file)

    return resultado

# Exemplo de uso
print(calculadora(10, 5, 'adição'))
print(calculadora(10, 9, 'divisão'))
