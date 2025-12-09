def agregar_producto(inventario):
    nombre = input("Nombre del producto: ").strip()
    cantidad = int(input("Cantidad: "))
    
    if nombre in inventario:
        inventario[nombre] += cantidad
        print(f" Se agregaron {cantidad} unidades a {nombre}")
        print(f"  Cantidad total: {inventario[nombre]}")
    else:
        inventario[nombre] = cantidad
        print(f" Producto {nombre} agregado con {cantidad} unidades")


def mostrar_inventario(inventario):
    if not inventario:
        print("\n El inventario está vacío")
        return
    
    print("INVENTARIO DE PRODUCTOS")

    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")



def buscar_producto(inventario):
    nombre = input("Nombre del producto a buscar: ").strip()
    
    if nombre in inventario:
        print(f" {nombre}: {inventario[nombre]} unidades")
    else:
        print(f" El producto '{nombre}' no existe en el inventario")


def menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar/Actualizar producto")
    print("2. Mostrar inventario completo")
    print("3. Buscar producto")
    print("4. Salir")

inventario = {}

while True:
    menu()
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        buscar_producto(inventario)
    elif opcion == "4":
        print("\n ¡Hasta luego!")
        break
    else:
        print(" Opción inválida.")