class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, stock: int):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def agregar_stock(self, cantidad: int):
        self.stock += cantidad

    def retirar_stock(self, cantidad: int):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock para retirar.")

    def mostrar_info(self):
        total_inventario = self.precio * self.stock
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}, Valor total en inventario: {total_inventario}")