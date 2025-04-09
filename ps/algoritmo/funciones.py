def mostrar_menu():
    print("¿Qué desea hacer?")
    print("1. Registrar un producto nuevo")
    print("2. Agregar stock a un producto existente")
    print("3. Retirar stock de un producto")
    print("4. Mostrar información de un producto")
    print("5. Finalizar el programa")

def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def validar_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def buscar_producto(nombre, productos):
    for producto in productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None