import pandas as pd
 
 #Escribir una funcom que reciba un diccionaro con las notas de los estudiantes del curso y devuelve una serie con el minimo,maximo,minimo,media, desvicaicon tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(),
    notas.std()], index=['Min' , 'Max' , 'Media' , 'Desviacion Estandar'])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas [notas >= 6].sort_values(ascending=False)


notas = {'Juan': 5.9, 'Juanita' : 5 ,'Pedro' : 6.6 ,'Fabian' : 8.5 ,
         'Maximialno' : 7.5 ,'Sandra' : 9.8 ,'Rosaro' : 9 ,}
print(estadistica_notas(notas))

print(aprobados(notas))