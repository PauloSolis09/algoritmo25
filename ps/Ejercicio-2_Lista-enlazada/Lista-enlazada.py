class Estacion: #representa una estacion individual
    def __init__(self, nombre, tiempo_a_siguiente=None):
        self.nombre = nombre
        self.tiempo_a_siguiente = tiempo_a_siguiente  # en minutos

#representacion de un noto de lista simplee
class NodoEstacion:
    def __init__(self, estacion):
        self.estacion = estacion
        self.siguiente = None

#representa toda las lista enlasada de estaciones
class Ruta:
    def __init__(self):
        self.inicio = None

    def agregar_estacion(self, nombre, tiempo_a_siguiente=None):
        nueva_estacion = NodoEstacion(Estacion(nombre, tiempo_a_siguiente))
        if not self.inicio:
            self.inicio = nueva_estacion
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_estacion

    def mostrar_ruta(self):
        actual = self.inicio
        while actual:
            print(f"{actual.estacion.nombre}", end=" -> " if actual.siguiente else "")
            actual = actual.siguiente
        print()

    def calcular_tiempo(self, origen, destino):
        actual = self.inicio
        tiempo_total = 0
        en_ruta = False

        while actual:
            nombre_actual = actual.estacion.nombre

            if nombre_actual == origen:
                en_ruta = True

            if en_ruta:
                if nombre_actual == destino:
                    return tiempo_total
                if actual.estacion.tiempo_a_siguiente is None:
                    break  # Fin de la ruta sin llegar al destino
                tiempo_total += actual.estacion.tiempo_a_siguiente

            actual = actual.siguiente

        return None  # Si no se encuentra el destino

# ------------------------
# Ejemplo de uso:

ruta = Ruta()
ruta.agregar_estacion("Estación A", 5)
ruta.agregar_estacion("Estación B", 7)
ruta.agregar_estacion("Estación C", 4)
ruta.agregar_estacion("Estación D", 6)
ruta.agregar_estacion("Estación E")  # Última estación

ruta.mostrar_ruta()

origen = "Estación C"
destino = "Estación E"
tiempo = ruta.calcular_tiempo(origen, destino)

if tiempo is not None:
    print(f"Tiempo estimado de {origen} a {destino}: {tiempo} minutos")
else:
    print(f"No se puede calcular el tiempo entre {origen} y {destino}")
