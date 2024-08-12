
import random
import numpy as np
import matplotlib.pyplot as plt

# Generar 100 ejemplos con restricciones lógicas
data = []
for _ in range(100):
    altura = round(random.uniform(1.5, 2.0), 2)  # Altura en metros
    peso = round(random.uniform(altura * 20, altura * 50), 2)  # Peso ajustado a la altura
    data.append((altura, peso))

# Separar datos en listas de altura y peso
alturas, pesos = zip(*data)

# Ajuste de una curva polinómica (por ejemplo, de grado 2)
coef = np.polyfit(alturas, pesos, 2)  # Ajusta un polinomio de grado 2
poly2d_fn = np.poly1d(coef)  # Genera la función polinómica

# Graficar los datos y la curva ajustada
plt.scatter(alturas, pesos)  # Gráfico de dispersión de los puntos
plt.plot(sorted(alturas), poly2d_fn(sorted(alturas)), color='red')  # Gráfico de la curva ajustada en rojo
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')
plt.title('Distribución de Peso y Altura con Curva de Ajuste')
plt.show()






# import random
# import pandas as pd

# # Función para generar datos aleatorios controlados
# def generar_datos(n):
#     datos = []
#     for _ in range(n):
#         estatura = round(random.uniform(1.4, 2.0), 2)  # Estatura entre 1.4 y 2.0 metros
#         peso = round(random.uniform(50, 100), 2)  # Peso entre 50 y 100 kilos
#         # Controlar valores extremos
#         while (estatura < 1.5 and peso > 80) or (estatura > 1.9 and peso < 60):
#             estatura = round(random.uniform(1.4, 2.0), 2)
#             peso = round(random.uniform(50, 100), 2)
#         datos.append((estatura, peso))
#     return datos

# # Generar 100 ejemplos
# datos = generar_datos(100)

# # Crear un DataFrame y guardarlo en un archivo CSV
# df = pd.DataFrame(datos, columns=['Estatura', 'Peso'])
# df.to_csv('datos.csv', index=False)
# print(df)
