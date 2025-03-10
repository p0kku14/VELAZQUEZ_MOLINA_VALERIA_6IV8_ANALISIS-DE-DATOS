import pandas as pd
##Ptograma que pregunte el usuario un rango de años y muestra en la panatlla una serie

inicio = int(input('Introduce el año de ventas inicial:'))
fin = int(input('Interoduce el año final de ventas'))

ventas = {}

for i in  range(inicio,fin+1):
    ventas [i] = float(input('introduce las ventas del año:' + str(i)
    + ':'))
ventas = pd.Series(ventas)
print('Ventas \n' , ventas)
print('ventas con descuento\n' , ventas *0.9)