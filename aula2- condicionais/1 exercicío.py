# 1 - Crie uma aplicação capaz de identificar a faixa etária com
# base na idade informada pelo usuário. Considere os seguintes critérios:
# Se a idade informada for maior ou igual a 0 e menor que 15, exibir a mensagem “Criança”.
# Se a idade informada for maior ou igual a 15 e menor que 30, exibir a mensagem “Jovem”.
# Se a idade informada for maior ou igual a 30 e menor que 60, exibir a mensagem “Adulto”.
# Se a idade informada for maior ou igual a 60, exibir a mensagem “Idoso”.

def identificar_faixa_etaria(idade):
    if idade >= 0 and idade < 15:
        return "Criança"
    elif idade >= 15 and idade < 30:
        return "Jovem"
    elif idade >= 30 and idade < 60:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

# Solicitando a idade do usuário
idade = int(input("Digite sua idade: "))

# Identificando a faixa etária
faixa_etaria = identificar_faixa_etaria(idade)

# Exibindo a faixa etária
print(f"Você é considerado(a): {faixa_etaria}")
