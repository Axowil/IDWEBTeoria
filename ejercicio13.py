"""
Crear una función primos_en_rango(inicio, fin) que reciba dos números y devuelva una lista con todos
los números primos entre inicio y fin
"""
#Definir funciones de primos 
def es_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def primos_en_rango(inicio, fin):
    primos = []
    
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    
    return primos
# Programa principal
inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

resultado = primos_en_rango(inicio, fin)

print(f"\nNúmeros primos entre {inicio} y {fin}:")
print(resultado)
print(f"Total de primos encontrados: {len(resultado)}")
