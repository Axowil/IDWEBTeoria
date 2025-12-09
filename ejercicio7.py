"""
Mismo programa anterior pero que sea iterativo y donde no se confíe en el usuario
"""
#funciones validar y suma de Pares 
def esPositivo(numero) :
    return numero > 0

def sumaPares(num):
#iteracion
    suma = 0 
    i = 2 
    while i <=num :
        suma+= i
        i +=2
    return suma

def obtenerNumeroValido():
    while True:
            numero = int(input('Introducir el numero: '))
            if esPositivo(numero):
                return numero
            else:
                print('El numero debe ser positivo. Intente nuevamente.')
                
# llamar a las funciones
introducir_numero = obtenerNumeroValido()
resultado = sumaPares(introducir_numero)
print(f'La suma de pares hasta {introducir_numero} es {resultado}')
