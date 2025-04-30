#Elaborado 30/04/2025
#anticopyrich
#Enoc Salinas
#Paulo solis
#Julio salamanca


def separarParImpar(pila):
    pares = []
    impares = []

    # Separamos los pares e impares usando otra pila
    while pila:
        numero = pila.pop()
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    # Primero agregamos los pares (parte inferior de la pila)
    for num in reversed(pares):
        pila.append(num)

    # Luego los impares (parte superior de la pila)
    for num in reversed(impares):
        pila.append(num)

    return pila


# Ejemplo de uso
pila = [2, 3, 6, 8, 11, 13, 18, 21]  # Tope es el final de la lista
resultado = separarParImpar(pila)
print("Pila salida:", resultado)
