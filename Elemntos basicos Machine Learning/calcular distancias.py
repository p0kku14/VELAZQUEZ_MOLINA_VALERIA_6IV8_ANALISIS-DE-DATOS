import numpy as np
import pandas as pd
from scipy.spatial import distance


puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1),  
}

df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print("Coordenadas de los puntos:")
print(df_puntos)

def calcular_distancias(df):
    distancias_euclidiana = pd.DataFrame(index=df.index, columns=df.index)
    distancias_manhattan = pd.DataFrame(index=df.index, columns=df.index)
    distancias_chebyshev = pd.DataFrame(index=df.index, columns=df.index)
    
    for i in df.index:
        for j in df.index:
            if i != j: 
                distancias_euclidiana.loc[i, j] = distance.euclidean(df.loc[i], df.loc[j])
                
             
                distancias_manhattan.loc[i, j] = distance.cityblock(df.loc[i], df.loc[j])
                
                distancias_chebyshev.loc[i, j] = distance.chebyshev(df.loc[i], df.loc[j])
    
    return distancias_euclidiana, distancias_manhattan, distancias_chebyshev

distancias_euclidiana, distancias_manhattan, distancias_chebyshev = calcular_distancias(df_puntos)

def encontrar_extremos(distancias):
    dist_sin_nan = distancias.copy()
    np.fill_diagonal(dist_sin_nan.values, np.nan)
    
  
    valor_maximo = dist_sin_nan.max().max()
    col_max = dist_sin_nan.max().idxmax()
    fila_max = dist_sin_nan[col_max].idxmax()
    
    
    valor_minimo = dist_sin_nan.replace(0, np.nan).min().min()
    col_min = dist_sin_nan.replace(0, np.nan).min().idxmin()
    fila_min = dist_sin_nan[col_min].replace(0, np.nan).idxmin()
    
    return valor_minimo, fila_min, col_min, valor_maximo, fila_max, col_max


print("\n=== DISTANCIA EUCLIDIANA ===")
print("Tabla de distancias:")
print(distancias_euclidiana)

min_euc, p1_min_euc, p2_min_euc, max_euc, p1_max_euc, p2_max_euc = encontrar_extremos(distancias_euclidiana)
print(f"\nPuntos más cercanos: {p1_min_euc} y {p2_min_euc} con distancia: {min_euc:.2f}")
print(f"Puntos más alejados: {p1_max_euc} y {p2_max_euc} con distancia: {max_euc:.2f}")

print("\n=== DISTANCIA MANHATTAN ===")
print("Tabla de distancias:")
print(distancias_manhattan)

min_man, p1_min_man, p2_min_man, max_man, p1_max_man, p2_max_man = encontrar_extremos(distancias_manhattan)
print(f"\nPuntos más cercanos: {p1_min_man} y {p2_min_man} con distancia: {min_man:.2f}")
print(f"Puntos más alejados: {p1_max_man} y {p2_max_man} con distancia: {max_man:.2f}")

print("\n=== DISTANCIA CHEBYSHEV ===")
print("Tabla de distancias:")
print(distancias_chebyshev)

min_cheb, p1_min_cheb, p2_min_cheb, max_cheb, p1_max_cheb, p2_max_cheb = encontrar_extremos(distancias_chebyshev)
print(f"\nPuntos más cercanos: {p1_min_cheb} y {p2_min_cheb} con distancia: {min_cheb:.2f}")
print(f"Puntos más alejados: {p1_max_cheb} y {p2_max_cheb} con distancia: {max_cheb:.2f}")


print("\n=== RESUMEN COMPARATIVO ===")
print("Puntos más cercanos:")
print(f"- Euclidiana: {p1_min_euc} y {p2_min_euc} ({min_euc:.2f})")
print(f"- Manhattan: {p1_min_man} y {p2_min_man} ({min_man:.2f})")
print(f"- Chebyshev: {p1_min_cheb} y {p2_min_cheb} ({min_cheb:.2f})")

print("\nPuntos más alejados:")
print(f"- Euclidiana: {p1_max_euc} y {p2_max_euc} ({max_euc:.2f})")
print(f"- Manhattan: {p1_max_man} y {p2_max_man} ({max_man:.2f})")
print(f"- Chebyshev: {p1_max_cheb} y {p2_max_cheb} ({max_cheb:.2f})")