"""
Crear una función promedio_ponderado(notas, pesos) que reciba dos listas: notas y pesos, y
devuelva el promedio ponderado. El programa debe pedir al usuario las notas y los pesos de 3
asignaturas y mostrar el resultado
"""

def promedio_ponderado(notas, pesos):
    suma_ponderada = 0
    suma_pesos = 0
    
    for i in range(len(notas)):
        suma_ponderada += notas[i] * pesos[i]
        suma_pesos += pesos[i]
    
    return suma_ponderada / suma_pesos

# Interaccion con el usuario 
print("Ingresa las notas y pesos de 3 asignaturas:")

notas = []
pesos = []

for i in range(3):
    nota = float(input(f"Nota de la asignatura {i+1}: "))
    peso = float(input(f"Peso de la asignatura {i+1}: "))
    notas.append(nota)
    pesos.append(peso)
    
resultado = promedio_ponderado(notas, pesos)
print(f"\nEl promedio ponderado es: {resultado:.2f}")
