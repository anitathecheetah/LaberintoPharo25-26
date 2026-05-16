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
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

class TestNarnia(unittest.TestCase):
    def test_historia_narnia(self):
        director = Director()
        juego = director.procesar("laberintos/lab_narnia.json")
        personaje = juego.personaje
        
        # 1. El personaje debe ser Peter
        self.assertEqual(personaje.nombre, "Peter Pevensie")
        self.assertEqual(personaje.posicion.num, 1)

        hab1 = juego.obtener_habitacion(1)
        hab1.entrar(personaje)
        # La vida base es 100. Con la poción debería subir a 200.
        self.assertEqual(personaje.vidas, 200)

        # 2. Ir a la habitación 4 (Invierno Eterno) para coger el Cuerno de Susan
        puerta_1_4 = Este().obtener_de(hab1)
        puerta_1_4.abrir()
        puerta_1_4.entrar(personaje)
        personaje.moverse_a(juego.obtener_habitacion(4))
        
        hab4 = juego.obtener_habitacion(4)
        # El daño fue 5, pero la Armadura de Narnia que se recoge en la hab1 lo absorbe!
        # Por lo tanto, la vida sigue siendo 200
        self.assertEqual(personaje.vidas, 200)
        # La armadura empezó con 50 de defensa, ahora tiene 45
        self.assertEqual(personaje.defensas.defensa_actual, 45)
        
        # La llave (Cuerno) ya se activó al entrar en la habitación 4, 
        # desbloqueando la puerta entre 2 y 3.
        puerta_2_3 = Este().obtener_de(juego.obtener_habitacion(2))
        # Su estado debe ser Cerrada (ya no Bloqueada)
        self.assertTrue(puerta_2_3.esta_cerrada())
        self.assertEqual(str(puerta_2_3.estado), "Cerrada")

        # 3. Volver a la habitación 1 y luego ir a la 2
        puerta_1_4.entrar(personaje) # Volvemos a hab 1
        personaje.moverse_a(juego.obtener_habitacion(1))
        
        puerta_1_2 = Norte().obtener_de(juego.obtener_habitacion(1))
        puerta_1_2.abrir()
        puerta_1_2.entrar(personaje)
        personaje.moverse_a(juego.obtener_habitacion(2))
        
        hab2 = juego.obtener_habitacion(2)
        # Se equipa a Aslan y el Escudo
        self.assertEqual(personaje.defensas.nombre, "Aslan")
        self.assertEqual(personaje.defensas.sucesor.nombre, "Escudo de Papá Noel 🛡️")

        # 4. Ir a la habitación 3 (Batalla Final)
        puerta_2_3.abrir() # Antes no se podía, pero gracias al Cuerno, sí
        self.assertTrue(puerta_2_3.esta_abierta())
        
        puerta_2_3.entrar(personaje)
        personaje.moverse_a(juego.obtener_habitacion(3))
        # Al entrar en la 3, el Mediador (Juego) lanza el combate de la Bruja Blanca
        
        # 5. La Bruja debería haber muerto y el estado del juego debe ser Final (Victoria)
        self.assertIsInstance(juego.fase, Final)
        self.assertIn("Bruja Blanca", juego.fase.resultado)

if __name__ == '__main__':
    unittest.main()
