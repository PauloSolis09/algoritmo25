#Ejercisio 3 clase numero 6

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

    def mostrar(self):
        return self.items.copy()  # Desde fondo hasta tope


def convBinario(numero):
    if numero == 0:
        return [0]

    pila = Pila()

    while numero > 0:
        residuo = numero % 2
        pila.apilar(residuo)
        numero = numero // 2

    binario = []
    while not pila.esta_vacia():
        binario.append(pila.desapilar())

    return binario

# Programa principal (main)
entrada = 15
print(f"Entrada → {entrada}")
salida = convBinario(entrada)
print(f"Salida → {salida}")