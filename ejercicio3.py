"""
Calcular el área y perímetro de un círculo. Mostrar los resultados con dos decimales. (Área =
πr2, Perímetro = 2π*r)
"""
def area (radio) :
    #constante
    PI =3.1415
    return PI*radio**2

def perimetro (radio ):
    #constante
    PI = 3.1415
    return 2*PI*radio

#Introducir datos
introducir_radio = float(input("Introducir el valor del radio : "))

#asignar los valores
valor_area = area(introducir_radio)
valor_perimetro = area(introducir_radio)

#Mostrar
print(f"El area y perimetro respectivamente es {valor_area:.2f} , {valor_perimetro:.2f}")
