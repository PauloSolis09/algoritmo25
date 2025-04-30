#Ejercicio numero 2

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        raise Exception("Pila vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def mostrar(self):
        return self.items.copy()  # Mostrar del fondo al tope

    def __len__(self):
        return len(self.items)


def ordena(pila):
    auxiliar = Pila()

    while not pila.esta_vacia():
        temp = pila.desapilar()

        # Reordenar auxiliar para que los elementos más grandes queden en el fondo
        while not auxiliar.esta_vacia() and auxiliar.cima() > temp:
            pila.apilar(auxiliar.desapilar())

        auxiliar.apilar(temp)

    # Transferimos de auxiliar a pila para que quede en orden descendente
    while not auxiliar.esta_vacia():
        pila.apilar(auxiliar.desapilar())

    return pila


# Creamos la pila de ejemplo
p = Pila()
for num in [1, 3, 2, 4]:
    p.apilar(num)

print("Pila original:", p.mostrar())

# Ordenamos la pila
p = ordena(p)

print("Pila ordenada (mayor a menor):", p.mostrar())
