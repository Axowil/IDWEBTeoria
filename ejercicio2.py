#Introducir los productos
producto_1 = float(input("Introducir el precio del produto 1 :")) 
producto_2 = float(input("Introducir el precio del producto 2 :"))
producto_3 = float(input("Introducir el precio del producto 3 :"))

#Constantes
IGV = 0.18

#Calcular monto
suma_productos = producto_1+producto_2+producto_3
monto_total = suma_productos+IGV*suma_productos

#Mostrar
print(f"El monto total incluyendo el IGV es {monto_total:.2f} soles")