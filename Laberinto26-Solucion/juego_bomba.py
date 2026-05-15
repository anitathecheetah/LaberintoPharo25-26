from juego import Juego
from bomba import Bomba
from pared import Pared
from puerta import Puerta

class JuegoBomba(Juego):
    """
    Concrete Creator en el patrón Factory Method.
    Ahora usa el patrón Decorator en vez de herencia estática.
    """
    def fabricar_pared(self):
        return Bomba(Pared())
        
    def fabricar_puerta(self, lado1=None, lado2=None):
        return Bomba(Puerta(lado1, lado2))

