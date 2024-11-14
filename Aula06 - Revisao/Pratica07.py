print ("Calculo  do Tempo")

total_segundos = int (input ("Digite o valor em segundos:" ))
valor_horas = int (total_segundos / 3600)
valor_minutos = int ( (total_segundos - (valor_horas * 3600))/60)
valor_segundos = int (total_segundos % 60)
print (valor_horas,"H",valor_minutos,"M",valor_segundos,"S") 

