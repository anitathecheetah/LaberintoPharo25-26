from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from laberinto_factory import LaberintoFactory

class Juego:
    def __init__(self, factory=None):
        self.factory = factory or LaberintoFactory()
        self.laberinto = None
        self.bichos = []

    def fabricar_laberinto(self):
        return self.factory.fabricar_laberinto()

    def fabricar_habitacion(self, numero):
        return self.factory.fabricar_habitacion(numero)

    def fabricar_pared(self):
        return self.factory.fabricar_pared()

    def fabricar_puerta(self, lado1=None, lado2=None, abierta=False):
        return self.factory.fabricar_puerta(lado1, lado2, abierta)

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def obtener_habitacion(self, numero):
        if self.laberinto is None:
            return None
        return self.laberinto.obtener_habitacion(numero)

    def crear_laberinto_demo(self):
        laberinto = self.fabricar_laberinto()

        habitacion_1 = self.fabricar_habitacion(1)
        habitacion_2 = self.fabricar_habitacion(2)

        puerta = self.fabricar_puerta(habitacion_1, habitacion_2, abierta=False)

        habitacion_1.poner_en(Norte(), self.fabricar_pared())
        habitacion_1.poner_en(Sur(), self.fabricar_pared())
        habitacion_1.poner_en(Oeste(), self.fabricar_pared())
        habitacion_1.poner_en(Este(), puerta)

        habitacion_2.poner_en(Norte(), self.fabricar_pared())
        habitacion_2.poner_en(Sur(), self.fabricar_pared())
        habitacion_2.poner_en(Este(), self.fabricar_pared())
        habitacion_2.poner_en(Oeste(), puerta)


        laberinto.agregar_habitacion(habitacion_1)
        laberinto.agregar_habitacion(habitacion_2)

        self.laberinto = laberinto
        return laberinto