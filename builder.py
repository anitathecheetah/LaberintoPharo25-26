from agresivo import Agresivo
from bicho import Bicho
from habitacion import Habitacion
from juego import Juego
from laberinto import Laberinto
from pared import Pared
from perezoso import Perezoso
from puerta import Puerta


class Builder:
    def __init__(self):
        self.laberinto = Laberinto()
        self.juego = Juego()
        self.juego.laberinto = self.laberinto

    def fabricar_juego(self):
        self.juego.laberinto = self.laberinto
        return self.juego

    def fabricar_laberinto(self):
        self.laberinto = Laberinto()
        self.juego.laberinto = self.laberinto
        return self.laberinto

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta(self):
        return Puerta()

    def fabricar_agresivo(self):
        return Agresivo()

    def fabricar_perezoso(self):
        return Perezoso()

    def fabricar_habitacion(self, numero):
        habitacion = Habitacion(numero)

        habitacion.ponerEn("norte", self.fabricar_pared())
        habitacion.ponerEn("sur", self.fabricar_pared())
        habitacion.ponerEn("este", self.fabricar_pared())
        habitacion.ponerEn("oeste", self.fabricar_pared())

        self.laberinto.agregar_habitacion(habitacion)
        return habitacion

    def conectar_habitaciones(self, num1, orientacion1, num2, orientacion2):
        puerta = self.fabricar_puerta()

        lado1 = self.laberinto.obtener_habitacion(num1)
        lado2 = self.laberinto.obtener_habitacion(num2)

        if lado1 is None or lado2 is None:
            raise ValueError("No se puede crear la puerta entre habitaciones inexistentes")

        puerta.lado1 = lado1
        puerta.lado2 = lado2

        lado1.ponerEn(orientacion1, puerta)
        lado2.ponerEn(orientacion2, puerta)

        return puerta

    def fabricar_bicho_modo(self, modo, posicion):
        if modo.lower() == "agresivo":
            estrategia = self.fabricar_agresivo()
        elif modo.lower() == "perezoso":
            estrategia = self.fabricar_perezoso()
        else:
            raise ValueError("Modo de bicho no valido")

        habitacion = self.juego.obtener_habitacion(posicion)
        if habitacion is None:
            raise ValueError(f"No existe la habitacion {posicion} para ubicar el bicho")

        bicho = Bicho(estrategia)
        bicho.posicion = habitacion

        self.juego.agregar_bicho(bicho)
        self.laberinto.agregar_bicho(bicho)
        return bicho