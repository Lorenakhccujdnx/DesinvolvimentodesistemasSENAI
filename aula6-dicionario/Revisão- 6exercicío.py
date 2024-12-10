"""
6)Sucessor e antecessor, faça uma aplicação que colete um número digitado pelo usuário
 e logo em seguida mostre em ordem: o numero anterior a ele, o próprio número escolhido e o número sucessor a ele
"""

def mostrar_sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"Antecessor: {antecessor}")
    print(f"Número escolhido: {numero}")
    print(f"Sucessor: {sucessor}")

def main():
    try:
        numero = int(input("Digite um número: "))
        mostrar_sucessor_antecessor(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
