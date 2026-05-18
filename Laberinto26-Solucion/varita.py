from abc import ABC, abstractmethod
from hoja import Hoja

class Varita(ABC):
    """
    Interface Target (Varita) que el Cliente (Personaje) espera poder usar.
    """
    @abstractmethod
    def cambiar_modo(self):
        pass

class VaritaItem(Hoja):
    """
    Objeto físico de la Varita que se coloca en el laberinto.
    """
    def __init__(self, nombre="Varita de la Bruja Blanca 🪄"):
        super().__init__()
        self.nombre = nombre
        self.encontrada = False

    def entrar(self, alguien=None):
        self.encontrada = True
        nombre_alguien = alguien.nombre if alguien and hasattr(alguien, 'nombre') else "El personaje"
        print(f"\n✨ ¡{nombre_alguien} ha encontrado la {self.nombre}! ✨")
        print("Siente la poderosa magia helada del objeto en sus manos.")
        print("¡Peter podrá canalizar este poder mágico en el combate contra la Bruja Blanca! 🪄")
