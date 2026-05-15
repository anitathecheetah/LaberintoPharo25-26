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
from armadura import Armadura

class TestChainOfResponsibility(unittest.TestCase):
    def setUp(self):
        self.personaje = Personaje("TestHero", vidas=100)

    def test_dano_sin_armadura(self):
        self.personaje.recibir_dano(20)
        self.assertEqual(self.personaje.vidas, 80)

    def test_dano_con_armadura(self):
        armadura = Armadura("Peto de Cuero", 30)
        self.personaje.equipar_defensa(armadura)
        
        # El ataque es de 20. La armadura tiene 30. Absorbe todo.
        self.personaje.recibir_dano(20)
        self.assertEqual(self.personaje.vidas, 100)
        self.assertEqual(armadura.defensa_actual, 10)
        
        # Otro ataque de 20. La armadura tiene 10. Absorbe 10, pasan 10.
        self.personaje.recibir_dano(20)
        self.assertEqual(self.personaje.vidas, 90)
        self.assertEqual(armadura.defensa_actual, 0)
        
        # Otro ataque de 20. Armadura rota. Pasan 20.
        self.personaje.recibir_dano(20)
        self.assertEqual(self.personaje.vidas, 70)

    def test_dano_con_multiples_armaduras(self):
        armadura_ligera = Armadura("Cuero", 10)
        armadura_pesada = Armadura("Acero", 40)
        
        # La cadena es: Acero -> Cuero -> Personaje
        self.personaje.equipar_defensa(armadura_ligera)
        self.personaje.equipar_defensa(armadura_pesada)
        
        # Ataque 45. Acero bloquea 40 (se rompe). Cuero bloquea 5.
        self.personaje.recibir_dano(45)
        self.assertEqual(armadura_pesada.defensa_actual, 0)
        self.assertEqual(armadura_ligera.defensa_actual, 5)
        self.assertEqual(self.personaje.vidas, 100)

    def test_armadura_en_habitacion_json(self):
        director = Director()
        # Creamos un json al vuelo o usamos uno cargado
        juego = director.procesar("laberintos/lab_armadura.json")
        personaje = juego.personaje
        hab1 = juego.obtener_habitacion(1)
        
        self.assertEqual(personaje.defensas, personaje) # Inicialmente no tiene armadura
        
        # Al entrar en la habitación, el personaje debería equiparse la armadura
        hab1.entrar(personaje)
        self.assertNotEqual(personaje.defensas, personaje)
        self.assertEqual(personaje.defensas.nombre, "Escudo Divino")

if __name__ == '__main__':
    unittest.main()
