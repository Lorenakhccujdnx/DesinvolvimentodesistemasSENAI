letras = set()

while True :
    letra = input("Digite uma letra:")
    letras.add(letra.lower())
    if "p" in letras :
        print("Parabéns você achou uma das letras!")
        break

    print ("Tente novamente.")
    print (f"Palavaras tentadas : {letras}")
# LOWER - TRANSFORMA TODAS AS LETRAS DA STRING EM MINÚSCULA

    