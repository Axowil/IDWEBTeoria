"""
Mostrar si un número es positivo, negativo o cero
"""
#Introducir datos 

numero = float(input("Introducir un numero : "))

#condicional 

if numero < 0 :
    print(f"El {numero} es negativo")
elif numero == 0 :
    print(f"El {numero} es cero")
else :
    print(f"El {numero} es positivo")

