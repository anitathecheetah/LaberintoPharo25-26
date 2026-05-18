import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from llave import Llave
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from estado_puerta import Bloqueada, Cerrada
from juego import Juego
from personaje import Personaje

class TestLlaveExtension(unittest.TestCase):
    def test_llave_desbloquea_puerta_en_juego(self):
        """Verifica que al recoger la Llave (Cuerno) se desbloquea dinámicamente su puerta asociada."""
        juego = Juego()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        puerta = Puerta(hab1, hab2)
        puerta.estado = Bloqueada()
        
        hab1.poner_en(Norte(), puerta)
        juego.laberinto = juego.fabricar_laberinto()
        juego.laberinto.agregar_habitacion(hab1)
        juego.laberinto.agregar_habitacion(hab2)
        
        personaje = Personaje("Susan", vidas=100)
        personaje.juego = juego
        personaje.posicion = hab1
        
        llave = Llave(1, 2, "Cuerno de Susan")
        
        self.assertIsInstance(puerta.estado, Bloqueada)
        
        # Susan entra en contacto con la Llave, lo que busca la cerradura y desbloquea la puerta
        llave.entrar(personaje)
        
        self.assertIsInstance(puerta.estado, Cerrada)
        self.assertTrue(llave.encontrada)

if __name__ == '__main__':
    unittest.main()
