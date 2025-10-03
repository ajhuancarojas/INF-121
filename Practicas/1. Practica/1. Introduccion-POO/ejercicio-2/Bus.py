class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajero = 0
        self.costo = 1.50
    def subir_pasajeros(self, cantidad):
        if self.pasajero + cantidad <= self.capacidad:
            self.pasajero += cantidad
            print(f"{cantidad} subieron al bus")
        else:
            print("No hay asientos suficientes.")

    def cobrar_pasaje(self):
        return self.pasajero * self.costo

    def asientos_disponibles(self):
        return self.capacidad - self.pasajero

c = Bus(50)
c.subir_pasajeros(15)
c.subir_pasajeros(25)
print("Asientos disponibles:", c.asientos_disponibles())
print("Total a cobrar: Bs.", c.cobrar_pasaje())
