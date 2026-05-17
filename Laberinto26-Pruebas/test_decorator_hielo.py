import unittest
import sys
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from armario import Armario
from hielo import Hielo
from personaje import Personaje
from llave import Llave

class TestDecoratorHielo(unittest.TestCase):

    def setUp(self):
        # Configuramos un armario base y lo decoramos con Hielo
        self.armario_base = Armario()
        self.armario_congelado = Hielo(self.armario_base, dano=5)
        self.personaje = Personaje("Peter")

    def test_decorator_aplica_dano(self):
        """Verifica que el Decorator Hielo resta vida al entrar."""
        vidas_iniciales = self.personaje.vidas
        
        # El personaje entra al armario congelado
        self.armario_congelado.entrar(self.personaje)
        
        # Debería haber perdido 5 de vida
        self.assertEqual(self.personaje.vidas, vidas_iniciales - 5)

    def test_decorator_agrega_hijo(self):
        """Verifica que el método puente agregarHijo funciona correctamente."""
        llave = Llave(1, 2, "Llave de prueba")
        
        # Añadimos la llave al armario DECORADO
        self.armario_congelado.agregarHijo(llave)
        
        # Verificamos que la llave se guardó realmente dentro del armario base
        self.assertIn(llave, self.armario_base.hijos)

if __name__ == '__main__':
    unittest.main()
