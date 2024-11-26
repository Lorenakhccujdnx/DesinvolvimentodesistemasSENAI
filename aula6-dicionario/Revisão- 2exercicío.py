#2)Programe um algoritmo onde podemos colocar um valor em reais 
# e logo a pós perguntar qual moeda deseja converter
#  ( Dólares, Ienes ou euro) e logo após isso 
# fazermos a conversão

def converter_moeda():
    # Taxas de conversão real
    taxas_de_conversao = {
        "USD": 5.85,  # 1 Dólar = 5.85 Reais
        "JPY": 0.038,  # 1 Iene = 0.038 Reais
        "EUR": 6.07   # 1 Euro = 6.07 Reais
    }

    # Entrada do valor em reais
    valor_em_reais = float(input("Digite o valor em reais: "))

    # Menu para escolha da moeda
    print("Escolha a moeda de destino:")
    print("1 - Dólares (USD)")
    print("2 - Ienes (JPY)")
    print("3 - Euros (EUR)")
    
    escolha_moeda = int(input("Digite o número correspondente à moeda: "))

    # Conversão de acordo com a escolha
    if escolha_moeda == 1:
        valor_convertido = valor_em_reais / taxas_de_conversao["USD"]
        moeda = "Dólares"
    elif escolha_moeda == 2:
        valor_convertido = valor_em_reais / taxas_de_conversao["JPY"]
        moeda = "Ienes"
    elif escolha_moeda == 3:
        valor_convertido = valor_em_reais / taxas_de_conversao["EUR"]
        moeda = "Euros"
    else:
        print("Opção inválida!")
        return

    # Saída do valor convertido
    print(f"O valor convertido é: {valor_convertido:.2f} {moeda}")

# Chamar a função para executar o algoritmo
converter_moeda()
