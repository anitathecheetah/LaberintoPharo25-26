from contenedor import Contenedor
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.orientaciones = [Norte(), Sur(), Este(), Oeste()]
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self, alguien=None):
        print(f"Has entrado en la habitacion {self.num}")

    def poner_en(self, orientacion, elemento):
        # El patrón Strategy en accion delegando a la orientación
        orientacion.poner_en(self, elemento)

    def mostrar_orientaciones(self):
        for o in self.orientaciones:
            elem = o.obtener_de(self)
            print(f"{type(o).__name__}: {type(elem).__name__ if elem else None}")

