# 3)Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.
# O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:

# dicas :
# "Muito alto!" se o palpite for maior que o número.
# "Muito baixo!" se o palpite for menor que o número.
# "Parabéns, você acertou!" se o palpite for igual ao número.
# Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
# Utilize a biblioteca random para gerar o número secreto.

import random

tentativas = 5

numero_secreto = random.randint(1, 100)

for i in range(tentativas):
    palpite = int(input(f"Tentativa {i+1}: "))

    if palpite > numero_secreto:
        print("Muito alto!")
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        palpite = numero_secreto
        print("Parabéns, você acertou!")
    
    if palpite!= numero_secreto:
        tentativas -= 1
        if tentativas == 0:
            print(f"Game Over! O número era {numero_secreto}")
            break

