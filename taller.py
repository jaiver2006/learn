import numpy as np
import pandas as pd


# Notas de un grupo
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

print("Notas:", notas)
print("Promedio:", np.mean(notas))
print("Máximo:", np.max(notas))
print("Mínimo:", np.min(notas))
print("Desviación estándar:", np.std(notas))




# Ventas de una tienda
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
ventas_con_aumento = ventas * 1.10
total_semana = np.sum(ventas_con_aumento)

print("\nVentas originales:", ventas)
print("Ventas con aumento del 10%:", ventas_con_aumento)
print("Total de la semana con aumento:", total_semana)




# Pronóstico del clima
celsius = np.array([18, 22, 25, 19, 30])
fahrenheit = celsius * 9 / 5 + 32

print("\nTemperaturas en Celsius:", celsius)
print("Temperaturas en Fahrenheit:", fahrenheit)




# Calificaciones por estudiante y materia
calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],  # Carlos
    [6.0, 7.5, 8.0, 7.0],  # Ana
    [9.0, 8.5, 9.5, 9.0],  # Luis
])

promedio_estudiantes = calificaciones.mean(axis=1)
promedio_materias = calificaciones.mean(axis=0)

print("\nPromedio de Carlos, Ana y Luis:", promedio_estudiantes)
print("Promedio de cada materia:", promedio_materias)
