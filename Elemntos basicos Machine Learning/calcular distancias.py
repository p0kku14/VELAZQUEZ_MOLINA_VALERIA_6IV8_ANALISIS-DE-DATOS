#calcularemos la distancia entre todos los pares del puntos y determinamos cuales etan mas alejados entre si y cuales estan mas crcanos utilizando las distancias euclidania,manhattan,chebyshev
import numpy as np
import pandas as pd
from scipy.spatial import distance
#Definimos las coordenadas
puntos={
    'Punto A': (2,3),
    'Punto B' :(5,4),
    'Punto C':(1,1),
    'Punto D':(6,7,),
    'Punto E':(3,5), 
      'Punto F':(8,2), 
      'Punto G':(4,6),
      'Punto E':(2,1),  
}

#Convertir las coodernadas a un df para faciliar el acalule

df_puntos=pd.DataFrame(puntos).T
df_puntos.columns=['X','Y']
print ("coodenadas de las puntos:")
print(df_puntos)
def calcular_distancias(puntos):
    distancias=pd.DataFrame(index=df_puntos.index,columns=df_puntos.index)
    #calculo de distancias
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i!= k: #No calcula la distancia del mismo punto
                #distancia euclediana
                distancias.loc[i,k]=distance.euclidean(df_puntos.loc[i],df_puntos.loc[k])
                
    return distancias
distancias=calcular_distancias(puntos)
valor_maximo=distancias.values.max()
(punto1,punto2)=distancias.stack().idxmax()
print("tabla de distancias")
print(distancias)
print("valor_maximo",valor_maximo)
print("entre el punto",punto1,";y el punto",punto2)


#otra manera de obtenerlo
max_value=distancias.max().max()
#obtener columnas
col_max=distancias.max().idxmax()

id_max=distancias[col_max].idxmax()
print(f"Valor maximo: {max_value} ")
print(f"columnas: {col_max} ")
print(f"indice: {id_max} ")
