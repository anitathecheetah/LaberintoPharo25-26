from laberinto_factory import LaberintoFactory
from pared_bomba import ParedBomba
from puerta_bomba import PuertaBomba

class LaberintoBombasFactory(LaberintoFactory):
    def fabricar_pared(self):
        return ParedBomba()
        
    def fabricar_puerta(self, lado1=None, lado2=None, abierta=False):
        return PuertaBomba(lado1, lado2, abierta)
