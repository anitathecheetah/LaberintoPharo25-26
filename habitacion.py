from contenedor import Contenedor
from cuadrado import Cuadrado
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

class Habitacion(Contenedor):
    def __init__(self, num):
        # El patrón Bridge: delegamos las propiedades geométricas a un objeto Forma (Cuadrado)
        super().__init__(forma=Cuadrado())
        self.num = num
        self.orientaciones = self.forma.obtener_orientaciones() if self.forma else []
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

    def recorrer(self, bloque):
        super().recorrer(bloque)
        if self.norte: self.norte.recorrer(bloque)
        if self.sur: self.sur.recorrer(bloque)
        if self.este: self.este.recorrer(bloque)
        if self.oeste: self.oeste.recorrer(bloque)

    def aceptar(self, visitor):
        super().aceptar(visitor)
        if self.norte: self.norte.aceptar(visitor)
        if self.sur: self.sur.aceptar(visitor)
        if self.este: self.este.aceptar(visitor)
        if self.oeste: self.oeste.aceptar(visitor)

    def aceptar_contenedor(self, visitor):
        visitor.visitar_habitacion(self)
