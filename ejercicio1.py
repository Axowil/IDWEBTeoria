"""
Calcular la temperatura promedio del fin de semana en Arequipa
"""
# Introducir las cuatro temperaturas
sabado_max = float(input("Temperatura Máxima del Sábado °C: "))
sabado_min = float(input("Temperatura Mínima del Sábado °C: "))
domingo_max = float(input("Temperatura Máxima del Domingo °C: "))
domingo_min = float(input("Temperatura Mínima del Domingo °C: "))

# Calcular el promedio de las cuatro temperaturas
temperatura_promedio = (sabado_max + sabado_min + domingo_max + domingo_min) / 4

# Mostrar el promedio
print(f"La temperatura promedio del fin de semana es: {temperatura_promedio:.2f}°C")
