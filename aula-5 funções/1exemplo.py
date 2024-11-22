def soma (x, y, z):
    print (f"{x}, {y}, {z} / {x+y+z}")

# se colocar 'soma' na mesma reta de 'print' o código não será
# gerado, então ponha identação (espaço)
soma(4, 8 , 10)
# para somar os números não é preciso colocar o sinal,só a vírgula
soma(x = 4,y = 8, z = 10)
# o código poderá ser escrito das duas formas

# para gerar esse segundo código é necessário pôr o 1* como
# comentário ou gerar em outra new file 
def soma(x,y,z = None) :
    if z is not None :
        print (f"{x}, {y}, {z} / {x+y+z}")
    else :
        print ("Z não existe")
    