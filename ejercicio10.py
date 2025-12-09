"""
Crear una función mcd(a, b) que reciba dos números enteros y que devuelva su máximo
común divisor usando el algoritmo de Euclides
"""

def mcd(a, b):
    # Algoritmo de Euclides
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

# Interacion con el usuario
print('Introducir dos numeros enteros')
numero_1= int(input('Introducir el primer numero : '))
numero_2= int(input('Introducir el segundo numero : '))

resultado = mcd(numero_1,numero_2)

print(f'Usando el algoritmo de euclides de los numeros {numero_1} y el {numero_2} el resultado es {resultado}')
