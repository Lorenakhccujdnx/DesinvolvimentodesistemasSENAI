def exercicio3():

     # PYTHON - secreta
     # _ _ A _ _ B - 6 Tentativas
     # Digite uma letra

     # QUAL LETRA VAI TENTAR?
     tentativas = [6]
     palavra_secreta =  "Python"
     letras_p_secreta = set(palavra_secreta)
     letras_tentadas= set ()

     while tentativas > 0 and letras_p_secreta :
        # EXIBIR A PALAVRA
        palavra_exibida = []
        for letra in letras_p_secreta :
            if letra in letras_tentadas :
               palavra_exibida.append(letra)

        else :
            palavra_exibida.append ("_")
        print("Palavra", " ".join(palavra_exibida))

         # PEDIR UMA LETRA
        letra = input("Digite uma letra: ").upper()

        # VERIFICAR SE A LETRA JÁ FOI TENTADA
        letras_tentadas.add(letra)

        # VERIFICAR SE A LETRA É CORRETA
        if letra in letras_p_secreta :
            print(f"Parabéns! A letra {letra} está na palavra secreta!")
            letras_p_secreta.remove(letra)
   
        # O REMOVE É APLICAdO TANTO PRA SETS QUANTO PARA LISTAS
        else :
               print(f"Errou, tentente novamente. A letra {letra} não está na palavra secreta!")
               tentativas -= 1
               print(f"Vidas restantes : {tentativas}")

     # MENSAGEM DE PERDA/ OU GANHO
    # TENTATIVAS > 0 
        if not letras_p_secreta :
          print(f"Parabéns! Você acertou a palavra secreta! {palavra_secreta}")
        else :
         print(f"Você não conseguiu acertar a palavra secreta! {palavra_secreta}")
        # TIRA UMA TENTATIVA CASO ERRE
       
        # CTRL= Z - PRA RECUPERAR O QUE FOI APAGADO