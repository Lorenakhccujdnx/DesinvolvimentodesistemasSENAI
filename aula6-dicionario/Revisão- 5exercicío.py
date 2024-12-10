"""
5)aplicação que pegue o número de clientes em uma mesa, o valor total da conta e após isso divida
 a conta de forma igual a todos os clientes
"""

def dividir_conta(numero_clientes, valor_total):
    if numero_clientes > 0:
        valor_por_cliente = valor_total / numero_clientes
        return valor_por_cliente
    else:
        return "Número de clientes inválido."

def main():
    try:
        numero_clientes = int(input("Digite o número de clientes na mesa: "))
        valor_total = float(input("Digite o valor total da conta: "))
        
        valor_por_cliente = dividir_conta(numero_clientes, valor_total)
        
        if isinstance(valor_por_cliente, str):
            print(valor_por_cliente)
        else:
            print(f"Cada cliente deve pagar: R$ {valor_por_cliente:.2f}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
