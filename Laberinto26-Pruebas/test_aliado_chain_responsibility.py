import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from aliado import Aliado
from personaje import Personaje
from estado_ente import Muerto

class TestAliadoExtension(unittest.TestCase):
    def test_aliado_absorbe_y_se_sacrifica(self):
        """Verifica que el NPC Aliado intercepta y mitiga el daño protegiendo al personaje."""
        personaje = Personaje("Peter", vidas=100)
        aslan = Aliado("Aslan", escudo=50)
        
        # Equipamos a Aslan como primera línea de defensa
        personaje.equipar_defensa(aslan)
        
        # Ataque de 30: Aslan bloquea todo, su escudo baja a 20. El personaje sigue con 100 vidas.
        personaje.recibir_dano(30)
        self.assertEqual(aslan.escudo, 20)
        self.assertEqual(personaje.vidas, 100)
        
        # Ataque de 40: Aslan bloquea los 20 restantes, se sacrifica (Muere).
        # Los 20 de daño sobrantes llegan al personaje, dejándole en 80 vidas.
        personaje.recibir_dano(40)
        self.assertEqual(aslan.escudo, 0)
        self.assertEqual(personaje.vidas, 80)
        self.assertIsInstance(aslan.estado, Muerto)

if __name__ == '__main__':
    unittest.main()
