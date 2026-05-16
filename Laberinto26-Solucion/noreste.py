from orientacion import Orientacion

class Noreste(Orientacion):
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Noreste, cls).__new__(cls)
        return cls._instancia

    def poner_en(self, contenedor, elemento):
        contenedor.ne = elemento

    def obtener_de(self, contenedor):
        return getattr(contenedor, 'ne', None)
