from orientacion import Orientacion

class Oeste(Orientacion):
    def poner_en(self, contenedor, elemento):
        contenedor.oeste = elemento

    def obtener_de(self, contenedor):
        return contenedor.oeste
