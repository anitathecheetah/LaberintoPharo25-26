from builder import Builder
from agresivo import Agresivo
from bicho import Bicho
from habitacion import Habitacion
from laberinto import Laberinto
from pared import Pared
from perezoso import Perezoso
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste


class LaberintoBuilder(Builder):
    def __init__(self):
        self.laberinto = Laberinto()
        self.juego = None

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
        return self.laberinto

    def str_to_orientacion(self, orientacion_str):
        estrategias = {
            "norte": Norte(),
            "sur": Sur(),
            "este": Este(),
            "oeste": Oeste()
        }
        return estrategias.get(orientacion_str.lower())

    def fabricarHabitacion(self, num):
        from norte import Norte
        from sur import Sur
        from este import Este
        from oeste import Oeste

        habitacion = Habitacion(num)
        habitacion.poner_en(Norte(), self.fabricarPared())
        habitacion.poner_en(Sur(), self.fabricarPared())
        habitacion.poner_en(Este(), self.fabricarPared())
        habitacion.poner_en(Oeste(), self.fabricarPared())
        self.laberinto.agregar_habitacion(habitacion)
        return habitacion

    def fabricarPuerta(self, lado1=None, lado2=None):
        return Puerta(lado1, lado2, abierta=False)

    def fabricarPared(self):
        return Pared()

    def fabricarPuertaLado1Or1Lado2Or2(self, num1, or1, num2, or2):
        from norte import Norte
        from sur import Sur
        from este import Este
        from oeste import Oeste

        lado1 = self.laberinto.obtener_habitacion(num1)
        lado2 = self.laberinto.obtener_habitacion(num2)

        if lado1 is None or lado2 is None:
            raise ValueError("No se puede crear la puerta: falta una habitacion")

        puerta = self.fabricarPuerta(lado1, lado2)
        lado1.poner_en(self.str_to_orientacion(or1), puerta)
        lado2.poner_en(self.str_to_orientacion(or2), puerta)
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