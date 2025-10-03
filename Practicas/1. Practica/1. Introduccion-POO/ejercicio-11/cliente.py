class Cliente:
    def __init__(self, nombre, mesa):
        self.nombre = nombre
        self.mesa = mesa

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_mesa(self):
        return self.mesa

    def set_mesa(self, mesa):
        self.mesa = mesa

    def __del__(self):
        print("Objeto Cliente destruido.")

    def mostrar(self):
        print(f"Cliente: {self.nombre}   / Mesa: {self.mesa}")


class Pedido:
    def __init__(self, idPedido, estado):
        self.idPedido = idPedido
        self.estado = estado

    def get_idPedido(self):
        return self.idPedido

    def set_idPedido(self, idPedido):
        self.idPedido = idPedido

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def __del__(self):
        print("Objeto Pedido destruido.")

    def mostrar(self):
        print(f"Pedido : {self.idPedido}   / Estado: {self.estado}")

c1 = Cliente("Alejandra", 5)
p1 = Pedido(101, "Registrado")

c1.mostrar()
p1.mostrar()
