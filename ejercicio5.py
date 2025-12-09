"""
Crear un clasificación de edades y muestre si es niño (0-12), adolescente (13-17), adulto
(18-60) o adulto mayor (60+)
"""
#Introducir datos
edad = float(input('Introducir su edad : '))

#Clasificacion
if edad < 0:
    print("Edad no valida")
elif edad <= 12:
    print("Usted es un niño")
elif edad <= 17:
    print("Usted es un adolescente")
elif edad <= 60:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")
    