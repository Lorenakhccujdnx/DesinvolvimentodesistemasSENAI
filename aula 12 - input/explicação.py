# MÓDULOS PADRÃO DO PYTHON
# 
# dicas úteis
# 1- EVITE USAR NOMES DE VARIÁVEIS
# IGUAIS A IMPORTAÇÃO

# as APELIDO = ADICIONA APLEIDO NO IMPORT
# obs : EVITE COLOCAR APELIDOS QUE NÃO SEJAM DESCRITIVOS


# método 1 - puxa todo o método
import sys as sistema
# método 2 - puxa só uma função
from sys import exit as sair

# import - ele importa tudo 
# from - importa um arquivo selecionado

# metodo 3 - puxa um arquivo
import um_modulo_balacubacu 
from um_modulo_balacubacu import nome

print(sistema.platform)
print(um_modulo_balacubacu.msg())
print(nome)
# importou o nome de outro arquivo
print(sair)
# irá mostrar qual é a plataforma de python

#print(sys)
# print(sys.version)
# <module 'sys' (built-in)> 
# é um módulo pré pronto