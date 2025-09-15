import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, t):
        return Vector3D(self.x + t.x, self.y + t.y, self.z + t.z)

    def __rmul__(self, escalar):
        return Vector3D(escalar * self.x, escalar * self.y, escalar * self.z)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normal(self):
        norma = abs(self)
        if norma == 0:
            return None
        return Vector3D(self.x / norma, self.y / norma, self.z / norma)

    def __matmul__(self, t):
        return self.x * t.x + self.y * t.y + self.z * t.z

    def __xor__(self, t):
        return Vector3D(
            self.y * t.z - self.z * t.y,
            self.z * t.x - self.x * t.z,
            self.x * t.y - self.y * t.x
        )

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

a = Vector3D(2, 8, 7)
b = Vector3D(4, 5, 1)

print("a =", a)
print("b =", b)

print("suma de vectores  =", a + b)
print("multiplicacion por escalar  =", 3 * a)
print("longitud   =", abs(a))
print("normal   =", a.normal())
print("producto escalar  =", a @ b)
print("producto vectorial  =", a ^ b)
