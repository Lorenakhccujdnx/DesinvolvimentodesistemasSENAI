# 2) João Papo-de-Pescador, homem de bem, comprou um microcomputador
#para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar um multa de R$ 4,00 por quilo excedente. João precisa que você faça um fluxograma
#  que leia a variável P (peso de peixes) e verifique se há excesso. 
# Se houver, gravar na variável E (Excesso) e na variável M o valor da multa Que João deverá pagar.
#  Caso contrário mostrar tais variáveis com o conteúdo ZERO.

def calcular_excesso(peso_peixes):
    limite = 50
    multa_por_quilo = 4.0
    excesso = 0
    multa = 0

    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * multa_por_quilo

    return excesso, multa

def main():
    peso_peixes = float(input("Digite o peso dos peixes (em kg): "))
    excesso, multa = calcular_excesso(peso_peixes)

    print(f"Excesso: {excesso} kg")
    print(f"Multa: R$ {multa:.2f}")

if __name__ == "__main__":
    main()
