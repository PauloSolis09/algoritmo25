## Autores
## Julio Cesar Salamanca Ortiz
## Paulo Marcell Solis Diaz
## Fecha de realización: 09/04/2025

from algoritmo.Clases import Producto
from algoritmo.funciones import mostrar_menu, validar_entero, validar_flotante, buscar_producto

cont = 1
Products_List = []
print("Bienvenido al sistema de administración de inventario")

while cont == 1:
    mostrar_menu()
    userChoice = validar_entero("Seleccione una opción: ")

    if userChoice == 1:
        name = input("Introduzca el nombre del producto: ")
        categoria = input("Introduzca la categoría del producto: ")
        stock = validar_entero("Introduzca el stock inicial del producto: ")
        precio = validar_flotante("Introduzca el precio unitario del producto: ")
        
        nuevo_producto = Producto(name, categoria, precio, stock)
        Products_List.append(nuevo_producto)
        print("Producto registrado con éxito.")

    elif userChoice == 2:
        nombre_producto = input("Introduzca el nombre del producto al que desea agregar stock: ")
        producto = buscar_producto(nombre_producto, Products_List)
        if producto:
            cantidad = validar_entero("Introduzca la cantidad a agregar: ")
            producto.agregar_stock(cantidad)
            print("Stock actualizado con éxito.")
        else:
            print("Producto no encontrado.")

    elif userChoice == 3:
        nombre_producto = input("Introduzca el nombre del producto del que desea retirar stock: ")
        producto = buscar_producto(nombre_producto, Products_List)
        if producto:
            cantidad = validar_entero("Introduzca la cantidad a retirar: ")
            producto.retirar_stock(cantidad)
            print("Stock actualizado con éxito.")
        else:
            print("Producto no encontrado.")

    elif userChoice == 4:
        nombre_producto = input("Introduzca el nombre del producto para mostrar información: ")
        producto = buscar_producto(nombre_producto, Products_List)
        if producto:
            producto.mostrar_info()
        else:
            print("Producto no encontrado.")

    elif userChoice == 5:
        cont = 0
        print("El programa ha finalizado con éxito.")
    else:
        print("Opción no válida. Intente de nuevo.")