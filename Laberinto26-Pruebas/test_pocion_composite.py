import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from pocion import Pocion
from personaje import Personaje

class TestPocionExtension(unittest.TestCase):
    def test_pocion_cura_vida(self):
        """Verifica que el Cordial de Fuego (Poción) cura vida una sola vez al recogerse."""
        pocion = Pocion("Cordial de Lucía", curacion=45)
        personaje = Personaje("Lucy", vidas=50)
        
        # Recoge la poción
        pocion.entrar(personaje)
        self.assertEqual(personaje.vidas, 95)
        self.assertTrue(pocion.usada)
        
        # Si vuelve a pasar por el mismo sitio, una poción usada ya no cura más
        pocion.entrar(personaje)
        self.assertEqual(personaje.vidas, 95)

if __name__ == '__main__':
    unittest.main()
