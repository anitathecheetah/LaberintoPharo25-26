from builder import Builder
from agresivo import Agresivo
from bicho import Bicho
from habitacion import Habitacion
from laberinto import Laberinto
from pared import Pared
from perezoso import Perezoso
from puerta import Puerta


class LaberintoBuilder(Builder):
    def __init__(self):
        self.laberinto = Laberinto()
        self.juego = None

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto

    def fabricarHabitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.ponerEn("norte", self.fabricarPared())
        habitacion.ponerEn("sur", self.fabricarPared())
        habitacion.ponerEn("este", self.fabricarPared())
        habitacion.ponerEn("oeste", self.fabricarPared())
        self.laberinto.agregar_habitacion(habitacion)
        return habitacion

    def fabricarPuerta(self, lado1=None, lado2=None):
        return Puerta(lado1, lado2, abierta=False)

    def fabricarPared(self):
        return Pared()

    def fabricarPuertaLado1Or1Lado2Or2(self, num1, or1, num2, or2):
        lado1 = self.laberinto.obtener_habitacion(num1)
        lado2 = self.laberinto.obtener_habitacion(num2)

        if lado1 is None or lado2 is None:
            raise ValueError("No se puede crear la puerta: falta una habitacion")

        puerta = self.fabricarPuerta(lado1, lado2)
        lado1.ponerEn(or1.lower(), puerta)
        lado2.ponerEn(or2.lower(), puerta)
        return puerta

    def fabricarBichoModo(self, str_modo, posicion):
        if str_modo.lower() == "agresivo":
            modo = Agresivo()
        elif str_modo.lower() == "perezoso":
            modo = Perezoso()
        else:
            raise ValueError("Modo de bicho no valido")

        habitacion = self.juego.obtener_habitacion(posicion)
        if habitacion is None:
            raise ValueError(f"No existe la habitacion {posicion} para ubicar el bicho")

        bicho = Bicho(modo)
        bicho.posicion = habitacion
        self.juego.agregar_bicho(bicho)
        self.laberinto.agregar_bicho(bicho)
        return bicho

    def obtenerLaberinto(self):
        return self.laberinto