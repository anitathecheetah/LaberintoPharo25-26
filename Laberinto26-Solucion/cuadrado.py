from forma import Forma
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

class Cuadrado(Forma):
    """
    ConcreteImplementor en el patrón Bridge.
    Representa una forma cuadrada con 4 orientaciones básicas.
    """
    def __init__(self):
        self.norte = Norte()
        self.sur = Sur()
        self.este = Este()
        self.oeste = Oeste()

    def obtener_orientaciones(self):
        return [self.norte, self.sur, self.este, self.oeste]
    
    def obtener_nombre(self):
        return "Cuadrado"
    
    def num_orientaciones(self):
        return 4
    
    def __str__(self):
        return "Cuadrado(N, S, E, O)"
