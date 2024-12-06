arquivo = "main.txt"

# MODOS DO TEXTIOWRAPPER
# w (escrita)
# r (read) - ler o conteúdo
# x (criação)
# t (modo texto)
# w+, r+ (escrita e leitura)
# b (binário)
# readline - ler a linha

# metodo 1

#leitura = open(arquivo,"w")
#leitura.write("oi")
#leitura.close()

# método 2
with open(arquivo,"w+") as leitura :
    # write - escreve uma linha
    # writelines - escreve múltiplas linhas
    # seek - move cursor
    leitura.write("QUE TOP \n")
    leitura.write("LINHA 2 \n")
    leitura.seek(0,0) # volta o cursor para o início do arquivo
    # ele apaga so códigos da primeira linha pra "reeiniciar os códigos que foram escritos depois" 
    leitura.writelines(
        ("LINHA3\n", "LINHA4\n", "LINHA5\n")
    )

with open(arquivo,"r") as leitura :
    print(leitura.read())
    print(leitura.readline().strip)
    # strip - é pra tirar o espaço vazio da linha ou coluna
    # ex : texto = "###Bem-vindo###"
    #  texto_limpo = texto.strip("#")
    #  print(texto_limpo)
    #  # Isso imprimirá "Bem-vindo"


# leitura.write("Este é um arquivo de teste.\n")

print(type(leitura))
print (arquivo)