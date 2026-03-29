from juego import Juego
from pared_bomba import ParedBomba
from puerta_bomba import PuertaBomba

class JuegoBomba(Juego):
    """
    Concrete Creator en el patrón Factory Method.
    Sobreescribe el método de fabricación para devolver un ConcreteProduct distinto.
    """
    def fabricar_pared(self):
        return ParedBomba()
        
    def fabricar_puerta(self, lado1=None, lado2=None, abierta=False):
        return PuertaBomba(lado1, lado2, abierta)
