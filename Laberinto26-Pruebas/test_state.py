import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from juego import Juego
from bicho import Bicho
from personaje import Personaje
from armario import Armario
from habitacion import Habitacion
from fase import Inicial, Jugando, Final
from estado_ente import Vivo, Muerto

class TestState(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()

    def test_fase_inicial(self):
        self.assertIsInstance(self.juego.fase, Inicial)

    def test_transicion_jugando(self):
        # Al intentar entrar en una habitación, pasa a Jugando
        hab = Habitacion(1)
        per = Personaje("Hero", 100)
        self.juego.notificar(per, "entrar_habitacion", hab)
        self.assertIsInstance(self.juego.fase, Jugando)

    def test_condicion_victoria(self):
        hab = Habitacion(1)
        armario = Armario()
        hab.agregarHijo(armario)
        per = Personaje("Hero", 100)
        
        # Primero pasa a jugando e interactúa
        self.juego.notificar(per, "entrar_habitacion", hab)
        
        # Como entró a una habitación con armario, debería ganar
        self.assertIsInstance(self.juego.fase, Final)
        self.assertEqual(self.juego.fase.resultado, "¡Has Ganado!")

    def test_estado_ente_vivo_a_muerto(self):
        per = Personaje("Hero", 10)
        self.assertIsInstance(per.estado, Vivo)
        self.assertTrue(per.esta_vivo())

        per.recibir_dano(10)
        self.assertIsInstance(per.estado, Muerto)
        self.assertFalse(per.esta_vivo())

    def test_condicion_derrota(self):
        # Asignar juego al personaje para que pueda notificar
        per = Personaje("Hero", 10)
        per.juego = self.juego
        
        # Forzar transición a jugando
        self.juego.fase = Jugando(self.juego)
        
        per.recibir_dano(10) # Muere y notifica "derrotado"
        
        self.assertIsInstance(self.juego.fase, Final)
        self.assertEqual(self.juego.fase.resultado, "Has Muerto")

if __name__ == '__main__':
    unittest.main()
