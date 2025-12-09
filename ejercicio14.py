"""
Crear un programa que permita almacenar el nombre de varios estudiantes y sus notas en un
diccionario, donde la clave sea el nombre del estudiante y el valor sea su nota (0-20). Mostrar la lista
completa de estudiantes y notas, el nombre del estudiante con la nota más alta y el promedio de
todas las notas. Usar funciones
"""

def agregar_estudiantes():
    """Agregar estudiantes y sus notas"""
    estudiantes = {}
    cantidad = int(input("¿Cuántos estudiantes deseas registrar? "))
    
    for i in range(cantidad):
        nombre = input(f"Nombre del estudiante {i+1}: ")
        nota = float(input(f"Nota de {nombre} (0-20): "))
        estudiantes[nombre] = nota
    
    return estudiantes

#funcion mostrar
def mostrar_estudiantes(estudiantes):
    print("\n--- LISTA DE ESTUDIANTES ---")
    for nombre, nota in estudiantes.items():
        print(f"{nombre}: {nota}")

#funcion nota maxima
def nota_maxima(estudiantes):
    mejor = max(estudiantes, key=estudiantes.get)
    return mejor, estudiantes[mejor]

#funcion promedio
def calcular_promedio(estudiantes):
    return sum(estudiantes.values()) / len(estudiantes)


# PROGRAMA PRINCIPAL
estudiantes = agregar_estudiantes()
mostrar_estudiantes(estudiantes)

mejor_nombre, mejor_nota = nota_maxima(estudiantes)
print(f"\nEstudiante con nota más alta: {mejor_nombre} con {mejor_nota}")

promedio = calcular_promedio(estudiantes)
print(f"Promedio de notas: {promedio:.2f}")