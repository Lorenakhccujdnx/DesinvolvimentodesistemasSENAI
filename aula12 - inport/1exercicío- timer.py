# import time 
from time import sleep as timer
# para importar outro código coloque , ctime

segundos = int(input("Quantos segundos tem o timer:"))
# int - porque o timer só pode gerar números inteiros
for i in range (segundos,0, -1):
# range - denomina aonde você começa
    timer(1)
    print(f"{i} segundos")

print("Tempo esgotado!")