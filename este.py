from orientacion import Orientacion

class Este(Orientacion):
    def poner_en(self, contenedor, elemento):
        contenedor.este = elemento

    def obtener_de(self, contenedor):
        return contenedor.este
