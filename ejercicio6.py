"""
Crear un programa que pida un numero entero n y sume todos los números pares desde 1
hasta n
"""
# Introducir datos
numero = int(input('Introducir un numero: '))

# Lógica
i = 2 
suma = 0  # Inicializamos la suma en 0

#iteracion
while i <= numero:
    suma += i  
    i += 2     

print(f'La suma de los numeros pares desde 1 hasta {numero} es {suma}')
