import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from armario import Armario
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from juego import Juego
from habitacion import Habitacion
from personaje import Personaje

class TestVaritaAdapterExtension(unittest.TestCase):
    def test_varita_transforma_a_la_bruja_en_perezosa(self):
        """Verifica que Peter usa la Varita Mágica (BichoAdapter) en el último golpe para debilitar a la Bruja y vencerla."""
        juego = Juego()
        hab = Habitacion(1)
        armario = Armario()
        hab.agregarHijo(armario)
        
        # Bruja Blanca con 40 de vida y 10 de poder, empieza en Agresivo
        bruja = Bicho(Agresivo(), vidas=40, poder=10)
        bruja.nombre = "Bruja Blanca"
        armario.agregarHijo(bruja)
        
        peter = Personaje("Peter Pevensie", vidas=100, poder=20)
        peter.juego = juego
        peter.posicion = hab
        armario.padre = hab
        
        # Simulamos que Peter entra en el armario, lo que desata el combate
        armario.entrar(peter)
        
        # 1. La bruja debe haber muerto
        self.assertFalse(bruja.esta_vivo())
        # 2. En el último golpe (vidas <= 20), el combate debió usar la varita y cambiar su modo a Perezoso
        self.assertIsInstance(bruja.modo, Perezoso)
        # 3. Peter sobrevive con éxito
        self.assertTrue(peter.esta_vivo())

if __name__ == '__main__':
    unittest.main()
