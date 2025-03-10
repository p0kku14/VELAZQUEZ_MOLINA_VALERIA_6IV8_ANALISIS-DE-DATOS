import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Elementosbasicosestadisticos/housing.csv')

#mostrar las primeras 5 filas

print(df.head())

#mostrar las ultimas 5 filas

print(df.tail())

#mostrar una fila es especifico

print(df.iloc[7 ])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#obtener la media

mediadecuarto = df['total_rooms'].mean()
print(f'La media de los cuartos es:{mediadecuarto}')

medianacuarto = df['total_rooms'].median
print(f'La media de los cuartos es:{medianacuarto}')
      
salariototal = df[ 'population'].sum()
print(f'El salario total es de:{salariototal}')

filtrado=df[df['ocean_proximity']=='ISLAND']
print(filtrado)

#Graficar

plt.scatter(df['ocean_proximity' ] [:10 ],df['median_house_value' ][:10 ])

plt.ylabel('precio')
plt.xlabel('Aproximidad')
plt.title('grafica de dispersion de proximidad vs mar')

plt.show()