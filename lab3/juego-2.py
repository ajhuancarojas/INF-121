import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            intento = int(input("Adivina un numero entre 0-10: "))

            if not self.validaNumero(intento):
                print("Intenta de nuevo.")
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste   !!!!!!")
                self.actualizaRecord()
                return
            else:
                if self.quitaVida():
                    if intento > self.numeroAAdivinar:
                        print("El numero es menor.")
                    else:
                        print("El numero es mayor.")
                else:
                    print("No te quedan mas vidas. El numero era : ", self.numeroAAdivinar)

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 == 0:
                return True
            else:
                print("Numero invalido, debe ser par.")
                return False
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 != 0:
                return True
            else:
                print("Numero invalido, debe ser impar.")
                return False
        return False
j1 = JuegoAdivinaNumero(3)
j2 = JuegoAdivinaPar(3)
j3 = JuegoAdivinaImpar(3)
j1.juega()
j2.juega()
j3.juega()
