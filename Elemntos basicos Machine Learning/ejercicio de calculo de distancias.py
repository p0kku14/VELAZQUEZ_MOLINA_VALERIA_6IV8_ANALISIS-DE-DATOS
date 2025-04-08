import numpy as np
import itertools

# Definir los puntos
puntos = {
    'A': (2, 3),
    'B': (5, 4),
    'C': (1, 1),
    'D': (6, 7),
    'E': (3, 5),
    'F': (8, 2),
    'G': (4, 6),
    'H': (2, 1)
}

# Función para calcular la distancia euclidiana
def distancia_euclidiana(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Función para calcular la distancia de Manhattan
def distancia_manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

# Función para calcular la distancia de Chebyshev
def distancia_chebyshev(p1, p2):
    return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))

# Función para encontrar el par con la distancia mínima y máxima
def encontrar_min_max_distancia(distancias):
    min_distancia = float('inf')
    max_distancia = 0
    par_min = None
    par_max = None
    
    for par, distancia in distancias.items():
        if distancia < min_distancia:
            min_distancia = distancia
            par_min = par
        if distancia > max_distancia:
            max_distancia = distancia
            par_max = par
    
    return par_min, min_distancia, par_max, max_distancia

# Calcular todas las distancias para cada métrica
distancias_euclidiana = {}
distancias_manhattan = {}
distancias_chebyshev = {}

# Generar todas las combinaciones posibles de pares de puntos
pares = list(itertools.combinations(puntos.keys(), 2))

# Calcular las distancias para cada par
for par in pares:
    p1, p2 = puntos[par[0]], puntos[par[1]]
    
    # Euclidiana
    dist_euc = distancia_euclidiana(p1, p2)
    distancias_euclidiana[(par[0], par[1])] = dist_euc
    
    # Manhattan
    dist_man = distancia_manhattan(p1, p2)
    distancias_manhattan[(par[0], par[1])] = dist_man
    
    # Chebyshev
    dist_cheb = distancia_chebyshev(p1, p2)
    distancias_chebyshev[(par[0], par[1])] = dist_cheb

# Encontrar los pares con distancia mínima y máxima para cada métrica
par_min_euc, min_euc, par_max_euc, max_euc = encontrar_min_max_distancia(distancias_euclidiana)
par_min_man, min_man, par_max_man, max_man = encontrar_min_max_distancia(distancias_manhattan)
par_min_cheb, min_cheb, par_max_cheb, max_cheb = encontrar_min_max_distancia(distancias_chebyshev)

# Mostrar resultados
print("Resultados para los puntos:")
for punto, coords in puntos.items():
    print(f"Punto {punto}: {coords}")

print("\nDistancia Euclidiana:")
print(f"Puntos más cercanos: {par_min_euc[0]} y {par_min_euc[1]} con distancia {min_euc:.2f}")
print(f"Puntos más alejados: {par_max_euc[0]} y {par_max_euc[1]} con distancia {max_euc:.2f}")

print("\nDistancia Manhattan:")
print(f"Puntos más cercanos: {par_min_man[0]} y {par_min_man[1]} con distancia {min_man:.2f}")
print(f"Puntos más alejados: {par_max_man[0]} y {par_max_man[1]} con distancia {max_man:.2f}")

print("\nDistancia Chebyshev:")
print(f"Puntos más cercanos: {par_min_cheb[0]} y {par_min_cheb[1]} con distancia {min_cheb:.2f}")
print(f"Puntos más alejados: {par_max_cheb[0]} y {par_max_cheb[1]} con distancia {max_cheb:.2f}")

# Mostrar todas las distancias calculadas
print("\nDetalles de todas las distancias calculadas:")
print("\nDistancias Euclidianas:")
for par, dist in sorted(distancias_euclidiana.items(), key=lambda x: x[1]):
    print(f"Puntos {par[0]} y {par[1]}: {dist:.2f}")

print("\nDistancias Manhattan:")
for par, dist in sorted(distancias_manhattan.items(), key=lambda x: x[1]):
    print(f"Puntos {par[0]} y {par[1]}: {dist:.2f}")

print("\nDistancias Chebyshev:")
for par, dist in sorted(distancias_chebyshev.items(), key=lambda x: x[1]):
    print(f"Puntos {par[0]} y {par[1]}: {dist:.2f}")