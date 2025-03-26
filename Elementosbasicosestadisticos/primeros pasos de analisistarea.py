import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


proyecto1 = pd.read_csv('Elementosbasicosestadisticos/Copia de proyecto1.csv')
catologo_surcusal = pd.read_csv('C:\VELAZQUEZ_MOLINA_VALERIA_6IV8_ANALISIS-DE-DATOS\Elementosbasicosestadisticos\Copia de Catalogo_sucursal.csv')

Ventastotales = proyecto1['ventas_tot'].sum()
print(Ventastotales)

Clientesconadeudos = (proyecto1['B_adeudo']=='Con adeudo').sum()
adeudados = Clientesconadeudos/len(proyecto1)*100
print(adeudados)
Clientessinadeudos = (proyecto1['B_adeudo']=='Sin adeudo').sum()
noadeudados = Clientessinadeudos/len(proyecto1)*100
print(noadeudados)
# Cargar los archivos CSV
ruta_proyecto1 = 'Elementosbasicosestadisticos/Copia de proyecto1.csv'
ruta_catalogo_sucursal = 'C:\VELAZQUEZ_MOLINA_VALERIA_6IV8_ANALISIS-DE-DATOS\Elementosbasicosestadisticos\Copia de Catalogo_sucursal.csv'


proyecto1 = pd.read_csv(ruta_proyecto1)
catalogo_sucursal = pd.read_csv(ruta_catalogo_sucursal)


proyecto1['B_mes'] = pd.to_datetime(proyecto1['B_mes'], dayfirst=True)


ventas_por_mes = proyecto1.groupby('B_mes')['ventas_tot'].sum()

std_pagos_por_mes = proyecto1.groupby('B_mes')['pagos_tot'].std()

deuda_total = proyecto1['adeudo_actual'].sum()

utilidad_porcentaje = ((ventas_por_mes.sum() - deuda_total) / ventas_por_mes.sum()) * 100


proyecto1 = proyecto1.merge(catalogo_sucursal, on='id_sucursal')


ventas_por_sucursal = proyecto1.groupby('suc')['ventas_tot'].sum()

deuda_por_sucursal = proyecto1.groupby('suc')['adeudo_actual'].sum()

margen_utilidad = ((ventas_por_sucursal - deuda_por_sucursal) / ventas_por_sucursal) * 100


plt.figure(figsize=(12, 5))
ventas_por_mes.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(12, 5))
std_pagos_por_mes.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Desviación Estándar de los Pagos por Mes')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar de Pagos')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 8))
ventas_por_sucursal.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors, startangle=90)
plt.title('Ventas Totales por Sucursal')
plt.ylabel('')  
plt.show()

fig, ax1 = plt.subplots(figsize=(12, 5))

color = 'tab:blue'
ax1.set_xlabel('Sucursal')
ax1.set_ylabel('Deuda Total', color=color)
ax1.bar(deuda_por_sucursal.index, deuda_por_sucursal, color=color, alpha=0.6, label='Deuda Total')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Margen de Utilidad (%)', color=color)
ax2.plot(margen_utilidad.index, margen_utilidad, color=color, marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Margen de Utilidad')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Deuda Total vs. Margen de Utilidad por Sucursal')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print(f"Deuda total de los clientes: ${deuda_total:,.2f}")
print(f"Porcentaje de utilidad del comercio: {utilidad_porcentaje:.2f}%")