"""
3)  Faça um programa que pergunte a nota do aluno e responda se ele foi aprovado ou não (media 7 para aprovação)
"""
def verificar_aprovacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    try:
        nota = float(input("Digite a nota do aluno: "))
        status = verificar_aprovacao(nota)
        print(f"O aluno está: {status}")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
