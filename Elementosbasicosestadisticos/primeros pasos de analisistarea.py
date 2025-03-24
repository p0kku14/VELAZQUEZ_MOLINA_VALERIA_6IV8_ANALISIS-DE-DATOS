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




colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
plt.pie(Ventastotales), labels=nombres, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.show()
