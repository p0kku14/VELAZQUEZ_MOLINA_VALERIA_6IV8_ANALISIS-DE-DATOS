import numpy as np
import pandas as pd
from scipy.spatial import distance

#Definimos las coordenadas
tiendas={
    'Tienda A': (1,1),
    'Tienda B' :(1,5),
    'Tienda C':(7,1),
    'Tienda D':(3,3),
    'Tienda E':(4,8)    
}

#Convertir las coodernadas a un df para faciliar el acalule

df_tiendas=pd.DataFrame(tiendas).T
df_tiendas.columns=['X','Y']
print ("coodenadas dr las tiendas")
print(df_tiendas)

#Inicializamos un df para almacenar las distancia

distancias_eu=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)

#calculamos las distancias 

for  i in df_tiendas.index:
    for j in df_tiendas.index:
        #diatncia eucladiana
        distancias_eu.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        #ditamcia manhatan
        distancias_mh.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        #distancia chabyshey
        distancias_ch.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])
        
    #mostrar los resultados 
print("\nDistancias eucladianas  entre las tiendas:")
print(distancias_eu)
print("\nDistancias manhattan entre las tiendas:")
print(distancias_mh)
print("\nDistancias chebyshev entre las tiendas:")
print(distancias_ch)
    
    