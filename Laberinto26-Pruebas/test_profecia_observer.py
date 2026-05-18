import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from observador import ProfeciaNarnia
from juego import Juego
from aliado import Aliado

class TestObserverExtension(unittest.TestCase):
    def test_profecia_recibe_eventos(self):
        """Verifica que la Profecía de Narnia (Observer) responde de forma reactiva a eventos del Juego."""
        juego = Juego()
        profecia = ProfeciaNarnia()
        juego.agregar_observador(profecia)
        
        self.assertIn(profecia, juego.observadores)
        
        # Notificamos eventos simulados para asegurar que el despachador de eventos funciona sin excepciones
        try:
            juego.notificar_observadores("personaje_herido", None)
            juego.notificar_observadores("aliado_equipado", Aliado("Aslan"))
            juego.notificar_observadores("pocion_tomada", None)
            juego.notificar_observadores("llave_recogida", None)
        except Exception as e:
            self.fail(f"El despachador de eventos de Observer lanzó una excepción inesperada: {e}")

if __name__ == '__main__':
    unittest.main()
