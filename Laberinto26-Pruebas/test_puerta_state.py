import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from puerta import Puerta
from estado_puerta import Bloqueada, Cerrada

class TestEstadoPuertaExtension(unittest.TestCase):
    def test_puerta_bloqueada_flujo(self):
        """Verifica el comportamiento restrictivo del estado Bloqueada y su posterior transición."""
        puerta = Puerta()
        puerta.estado = Bloqueada()
        
        # Intentar abrir puerta bloqueada no hace nada, sigue bloqueada
        puerta.abrir()
        self.assertIsInstance(puerta.estado, Bloqueada)
        self.assertTrue(puerta.esta_cerrada())
        
        # Desbloquear puerta (pasa a Cerrada)
        puerta.estado = Cerrada()
        self.assertIsInstance(puerta.estado, Cerrada)
        
        # Abrir puerta cerrada (pasa a Abierta)
        puerta.abrir()
        self.assertTrue(puerta.esta_abierta())

if __name__ == '__main__':
    unittest.main()
