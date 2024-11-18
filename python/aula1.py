# AULA 1 - INTRODUÇÃO E VARIÁVEIS

# COMENTÁRIO

'''''
DOCSTRING - ANOTAÇÕES
'''''

# PRINT - ESCREVER 
print('Bom dia!!!')
print('Lorena')
# CRLF - caracteres que representam a quebra de linha do sistema
# \r return
#\n line feed (quebra de linha)

# end - final
print ('uma informação', 'importante', end = '\n')
# concatenar atrvés da ,
# sep dar espaço (é o separador do print)
print ('uma informação importante ',' importante', sep =  '-----')
print (123)

# type
print(type(1111111)) # int - numero inteiro 
print(type(1.1)) # float - numero real
print(type('xx')) # str/string - caracter
print(type('true')) # bool/ bolean - função logica - (true our false) verdadeiro ou falso

# variavel
# evitar 1 - caracteres especiais (ç, !)
 # evitar 2 - espaços vazios
 # camelCase = umExemplo (Java)
 # snakeCase = um_exemplo (Python)
 # evitar 3 - numeros solos ou começo de variavel ex : 1nome
 # evitar *4 - nomes pouco descritivos ex : emoji (vai travar, pois a variavel nao foi declarada

 # variaveis maiusculo são constantes
 # constante não ter seu valor mudado
teste = 'TESTE'
print ('teste')