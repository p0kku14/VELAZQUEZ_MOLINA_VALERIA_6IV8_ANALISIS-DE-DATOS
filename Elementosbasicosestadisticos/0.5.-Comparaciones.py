import numpy as np
import matplotlib.pyplot as plt

#vamos a crear un asemilla  random para reproductibilidad 
np.random.seed(0)

#vamos a buscar los datos apara una dsitribucion 
#media
media =  0
#desvaciones estandaar 
sigma1 = 1
sigma2 = 2
sigma3 = 3

#el numero de mustras para el analisis
n_muestras = 1000

#vamis a generar datos d las distribuciones normales
data1 = np.random.normal(media, sigma1 ,n_muestras)
data2 = np.random.normal(media, sigma2,n_muestras)
data3 = np.random.normal(media, sigma3 ,n_muestras)

#vamos a configurar la grafica 
plt.figure(figsize=(10,6))

#vamos a cargar las frecuenciias a partir de una grafica de histograma 
plt.hist(data1 , bins=30 , color='blue' , density=True , label='Desviacion estandar = 1', alpha=0.5)
plt.hist(data2 , bins=30 , color='red' , density=True , label='Desviacion estandar = 2', alpha=0.5)
plt.hist(data3 , bins=30 , color='green', density=True , label='Desviacion estandar = 3', alpha=0.5)

# a graficar 
plt.title('COMPARACION DE dISTRIBUCIONES nORMALES con una Semilla')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0 ,  color='black' , linewidth=0.5 , ls='--')
plt.axvline(0 ,  color='black' , linewidth=0.5 , ls='--')
plt.legend()
plt.grid()

plt.show()