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

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            intento = int(input("Adivina un numero entre 0-10: "))

            if intento == self.numeroAAdivinar:
                print("Acertaste   !!!!!!")
                self.actualizaRecord()
                return
            else:
                if self.quitaVida():
                    if intento > self.numeroAAdivinar:
                        print("El nUmero es menor.")
                    else:
                        print("El numero es mayor.")
                else:
                    print("No te quedan mas vidas. \nEl numero era :", self.numeroAAdivinar)

juego = JuegoAdivinaNumero(3)
juego.juega()
