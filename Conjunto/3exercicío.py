"""
3) Faça o jogo da forca em python utilizando o Set() como base!
"""
import random

def escolher_palavra():
    palavras = ['python', 'javascript', 'programacao', 'desenvolvedor', 'tecnologia']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_palavra = set(palavra)
    letras_adivinhadas = set()
    tentativas = 6

    while len(letras_palavra) > 0 and tentativas > 0:
        print('Palavra: ', ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra]))
        print('Letras adivinhadas: ', ' '.join(letras_adivinhadas))
        print(f'Tentativas restantes: {tentativas}')

        letra_adivinhada = input('Adivinhe uma letra: ').lower()

        if letra_adivinhada in letras_palavra:
            letras_palavra.remove(letra_adivinhada)
            letras_adivinhadas.add(letra_adivinhada)
        else:
            tentativas -= 1
            letras_adivinhadas.add(letra_adivinhada)

    if tentativas == 0:
        print(f'Você perdeu! A palavra era {palavra}.')
    else:
        print(f'Parabéns! Você adivinhou a palavra {palavra}.')

jogar_forca()
