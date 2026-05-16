import sys
import os
import unittest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from director import Director
from personaje import Personaje
from armario import Armario
from fase import Final

class TestNarnia(unittest.TestCase):
    def test_historia_narnia(self):
        director = Director()
        juego = director.procesar("laberintos/lab_narnia.json")
        personaje = juego.personaje
        
        # 1. El personaje debe ser Peter
        self.assertEqual(personaje.nombre, "Peter Pevensie")
        self.assertEqual(personaje.posicion.num, 1)

        # 2. Ir a la habitacion 2 y encontrar a Aslan
        hab2 = juego.obtener_habitacion(2)
        personaje.moverse_a(hab2) # Esto dispara "entrar_habitacion"
        hab2.entrar(personaje) # Para interactuar con los elementos de la habitación
        
        # Como hay un Aliado en hab2, debería estar en la cadena de defensas
        self.assertNotEqual(personaje.defensas, personaje)
        self.assertEqual(personaje.defensas.nombre, "Aslan")

        # 3. Entrar al armario de la habitación 2 para equiparse el escudo
        # hab2.entrar(personaje) ya ha recorrido los hijos y abierto el armario
        
        # Ahora debería tener "Aslan" en la cadena y también "Escudo y Espada"
        self.assertEqual(personaje.defensas.nombre, "Aslan")
        self.assertEqual(personaje.defensas.sucesor.nombre, "Escudo y Espada de Papá Noel")

        # 4. Ir a la habitación 3 y abrir el armario de la Bruja
        hab3 = juego.obtener_habitacion(3)
        personaje.moverse_a(hab3)
        
        # Forzar un poder alto a la Bruja y a Peter para el test
        # Al abrir la habitación (y por tanto el armario), la Bruja sale y empieza el combate
        hab3.entrar(personaje)
        
        # 5. La Bruja debería haber muerto (y Aslan sacrificar su escudo si el daño fue grande)
        # 6. El estado del juego debe ser Final (Victoria)
        self.assertIsInstance(juego.fase, Final)
        self.assertIn("Bruja Blanca", juego.fase.resultado)

if __name__ == '__main__':
    unittest.main()
