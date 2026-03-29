from orientacion import Orientacion

class Sur(Orientacion):
    def poner_en(self, contenedor, elemento):
        contenedor.sur = elemento

    def obtener_de(self, contenedor):
        return contenedor.sur
