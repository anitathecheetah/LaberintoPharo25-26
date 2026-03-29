from orientacion import Orientacion

class Norte(Orientacion):
    def poner_en(self, contenedor, elemento):
        contenedor.norte = elemento

    def obtener_de(self, contenedor):
        return contenedor.norte
