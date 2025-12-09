"""
Escribir una función invertir_cadena(cadena) que reciba un texto y devuelva el texto
invertido. Luego, pedir al usuario que ingrese una palabra o frase y mostrar el resultado
usando la función
"""

def invertir_cadena(cadena):
    cadena_nueva = ""
    for caracter in cadena:
        cadena_nueva = caracter + cadena_nueva  
    return cadena_nueva

# Pedir al usuario una frase
texto = input("Ingresa una palabra o frase: ")
resultado = invertir_cadena(texto)
print(f"Texto invertido: {resultado}")
