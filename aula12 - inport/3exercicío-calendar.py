# import calendar
# print (calendar.calendar(2024))
# irá mostrra todos os meses do ano de 2024

import calendar
from datetime import datetime

# criando um datetime com o ano atual

ano_atual = datetime.now().year 
dia_atual = datetime.now().day
mes_atual = datetime.now().month
hora_atual = datetime.now().hour 

# imprimindo o ano, dia, mês e hora atual
print(f"Você está no ano de: {ano_atual} \n dia: {dia_atual} \n mês: {mes_atual} \n hora: {hora_atual} ")
print (calendar.calendar(ano_atual))