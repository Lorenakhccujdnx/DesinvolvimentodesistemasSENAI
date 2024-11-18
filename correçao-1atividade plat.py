# Terá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

'''
ENTRADA
*PESO

PROCESSAMENTO
SE TEM MULTA (ACIMA DE 50)
VER EXCESSO (4 POR QUILO)
CALCULAR
SENAO
  MOSTRAR QUE NAO HA MULTA

SAIDA
  MOSTRAR O VALOR DA MULTA
'''

peso= float(input('Digite o peso:'))
peso_maximo = 50.00
multa = 4.00

if peso > peso_maximo:
   excesso = peso - peso_maximo
   multa_excesso = excesso * multa
   print(f'O valor total a ser pago é R $ {valor_total}')
else:
   print('Não há multa!')