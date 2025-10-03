class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Paterno: {self.paterno}")
        print(f"Materno: {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"CI: {self.ci}")

    def mayorDeEdad(self):
        return self.edad >= 18
    def modificarEdad(self, nueva_edad):
        self.edad = nueva_edad
    def mismoPaterno(self, otra_persona):
        return self.paterno == otra_persona.paterno

p1 = Persona("Pedro", "Perez", "Gomez", 20, "8335522")
p2 = Persona("Ana", "Perez", "Huanca", 24, "12345000")
p1.mostrarDatos()
print("Es mayor de edad:", p1.mayorDeEdad())
p2.mostrarDatos()
print("Es mayor de edad:", p2.mayorDeEdad())
print("Tienen el mismo paterno:", p1.mismoPaterno(p2))