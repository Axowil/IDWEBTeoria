"""
Escribir una función contar_vocales(texto) que reciba una cadena y devuelva el número de vocales
que contiene en total y cuantas de cada tipo
"""
#definir la funcion
def contar_vocales(texto):
    conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for caracter in texto.lower():
        if caracter in conteo:
            conteo[caracter] += 1
    
    return sum(conteo.values()), conteo

#Introducir los datos
cadena_texto = str(input('Introducir la frase : '))
resultado_vocales = contar_vocales(cadena_texto)

print(f'La cadena original es {cadena_texto} . \ny la cantidad de vocales respectivo es {resultado_vocales}')