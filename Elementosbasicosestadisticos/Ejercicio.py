import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcular_estadisticas(datos):
    return {
        'Min': datos.min(),
        'Max': datos.max(),
        'Media': datos.mean(),
        'Mediana': datos.median(),
        'Moda': datos.mode()[0] if not datos.mode().empty else np.nan,
        'Varianza': datos.var(ddof=1),
        'Desviacion Estandar': datos.std(ddof=1)
    }

def analizar_housing_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
        return
    
    columnas = ["median_house_value", "total_bedrooms", "population"]
    
    for col in columnas:
        if col in df:
            print(f"Estadísticas para {col}:")
            print(calcular_estadisticas(df[col].dropna()))
            print()
    
    df[columnas].dropna().hist(bins=30, alpha=0.5, figsize=(10, 6))
    plt.suptitle("Histogramas")
    plt.show()

# Ejecutar la función con el archivo
file_path = "VELAZQUEZ_MOLINA_VALERIA_6IV8_ANALISIS-DE-DATOS/Elementosbasicosestadisticos/housing.csv"
analizar_housing_data(file_path)