class Fruta:
    def __init__(self, nombre, tipo, nroVitaminas, v30):
        self.nombre = nombre
        self.tipo = tipo
        self.nroVitaminas = nroVitaminas
        self.v30 = v30

    def get_nombre(self): return self.nombre
    def get_tipo(self): return self.tipo
    def get_nroVitaminas(self): return self.nroVitaminas
    def get_v30(self): return self.v30

f1 = Fruta("uva", "subtropical", 3, "K, C, E")
print(f"Fruta 1: {f1.get_nombre()}, Tipo: {f1.get_tipo()}, Vitaminas: {f1.get_nroVitaminas()}, v30: {f1.get_v30()}")

f2 = Fruta("manzana", "temperada", 2, "A, C")
print(f"Fruta 2: {f2.get_nombre()}, Tipo: {f2.get_tipo()}, Vitaminas: {f2.get_nroVitaminas()}, voltaje0: {f2.get_v30()}")

f3 = Fruta("naranja", "citrico", 3, "C, A, B")
print(f"Fruta 3: {f3.get_nombre()}, Tipo: {f3.get_tipo()}, Vitaminas: {f3.get_nroVitaminas()}, v30: {f3.get_v30()}")