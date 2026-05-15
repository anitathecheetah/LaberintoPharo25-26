from abc import ABC, abstractmethod

class Varita(ABC):
    """
    Interface Target (Varita) que el Cliente (Personaje) espera poder usar.
    """
    @abstractmethod
    def cambiar_modo(self):
        pass
