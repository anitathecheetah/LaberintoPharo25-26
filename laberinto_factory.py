from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta

class LaberintoFactory:
    def fabricar_laberinto(self):
        return Laberinto()
        
    def fabricar_habitacion(self, numero):
        return Habitacion(numero)
        
    def fabricar_pared(self):
        return Pared()
        
    def fabricar_puerta(self, lado1=None, lado2=None):
        return Puerta(lado1, lado2)
