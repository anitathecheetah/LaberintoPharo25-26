from orientacion import Orientacion

class Este(Orientacion):
    _unicaInstancia = None

    def __new__(cls):
        if cls._unicaInstancia is None:
            cls._unicaInstancia = super().__new__(cls)
        return cls._unicaInstancia

    def poner_en(self, contenedor, elemento):
        contenedor.este = elemento

    def obtener_de(self, contenedor):
        return contenedor.este
