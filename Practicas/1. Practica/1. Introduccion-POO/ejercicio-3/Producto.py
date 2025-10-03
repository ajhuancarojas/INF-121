class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} u")
        else:
            print(f"No hay suficiente stock para vender {cantidad} u")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Restablecer: {cantidad} u")


c = Producto("CARNE", 50.5, 100)
print("Producto:", c.nombre)
print("Precio:", c.precio, "Bs.")
print("Stock:", c.stock)

c.vender(50)
c.reabastecer(7)

print("Producto:", c.nombre)
print("Precio:", c.precio, "Bs.")
print("Stock:", c.stock)
