arquivo = "teste.txt"

import json
usuario ={
    "nome" : "Emília",
    "idade" : 25,
    "cep" : "9700000-00"
    # usamos dicionário para fazer uma lista
}
# criar json
# jason.dump = 
with open("dados.json","w", encoding= "utf8") as leitura :
    # encoding= "utf8" --- Quando você usa encoding="utf8" no comando open(), está especificando que o arquivo deve ser lido 
    # ou escrito utilizando a codificação de caracteres UTF-8
    json.dump(
       usuario,
       leitura,
       indent = 2
    ) 
    # leitura.write("ATENÇÃO!!")

with open("dados.json","r", encoding= "utf8") as leitura :
    pessoa = json.load(leitura)
    print(pessoa["nome"])