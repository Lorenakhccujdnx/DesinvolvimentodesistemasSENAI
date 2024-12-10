"""
2) Solicite ao usuario um número de 1 a 7 e informe um dia da semana correspondente (ex: 1 = segunda feira)
"""

# Solicitar um número de 1 a 7
def dia_da_semana(numero):
    dias = {
        1: "Segunda-feira",
        2: "Terça-feira",
        3: "Quarta-feira",
        4: "Quinta-feira",
        5: "Sexta-feira",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero, "Número inválido. Por favor, digite um número de 1 a 7.")

def main():
    numero = int(input("Digite um número de 1 a 7: "))
    dia = dia_da_semana(numero)
    print(f"O dia correspondente é: {dia}")

if __name__ == "__main__":
    main()
