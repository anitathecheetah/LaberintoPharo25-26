import json
from laberinto_builder import LaberintoBuilder
from juego import Juego


class Director:
    def __init__(self):
        self._builder = None
        self._dict = None
        self._juego = None

    @property
    def builder(self):
        return self._builder

    @property
    def juego(self):
        return self._juego

    def procesar(self, archivo):
        self.leerArchivo(archivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()
        self.fabricarTuneles()
        self.fabricarPersonajes()
        
        self._juego.prototipo = self._juego.laberinto
        self._juego.laberinto = self._juego.clonar_laberinto()
        
        return self._juego

    def leerArchivo(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            self._dict = json.load(f)

    def iniBuilder(self):
        forma = self._dict.get("forma", "poligono4")

        if forma == "poligono4":
            self._builder = LaberintoBuilder()
        else:
            self._builder = LaberintoBuilder()

    def fabricarLaberinto(self):
        self._builder.fabricarLaberinto()

        laberinto_data = self._dict.get("laberinto", [])
        for elem in laberinto_data:
            self.fabricarLaberintoRecursivo(elem, None)

        puertas_data = self._dict.get("puertas", [])
        for puerta in puertas_data:
            self._builder.fabricarPuertaLado1Or1Lado2Or2(
                puerta[0], puerta[1], puerta[2], puerta[3]
            )

    def fabricarLaberintoRecursivo(self, dic, padre):
        tipo = dic.get("tipo", "")
        contenedor = padre

        if tipo == "habitacion":
            contenedor = self._builder.fabricarHabitacion(dic.get("num", 0))

        hijos = dic.get("hijos", [])
        for hijo in hijos:
            self.fabricarLaberintoRecursivo(hijo, contenedor)

    def fabricarJuego(self):
        self._juego = Juego()
        self._juego.laberinto = self._builder.obtenerLaberinto()
        self._builder.juego = self._juego

    def fabricarBichos(self):
        bichos_data = self._dict.get("bichos", [])

        for bicho_data in bichos_data:
            modo = bicho_data.get("modo", "Agresivo")
            posicion = bicho_data.get("posicion", 1)
            self._builder.fabricarBichoModo(modo, posicion)

    def fabricarTuneles(self):
        tuneles_data = self._dict.get("tuneles", [])
        for tunel_data in tuneles_data:
            pos = tunel_data.get("posicion", 1)
            ori = tunel_data.get("orientacion", "norte")
            self._builder.fabricarTunel(pos, ori)

    def fabricarPersonajes(self):
        personajes_data = self._dict.get("personajes", [])
        for p_data in personajes_data:
            nombre = p_data.get("nombre", "Heroe")
            pos = p_data.get("posicion", 1)
            self._builder.fabricarPersonaje(nombre, pos)

    def __str__(self):
        return f"Director con builder={self._builder}"