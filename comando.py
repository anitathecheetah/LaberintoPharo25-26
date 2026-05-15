from abc import ABC, abstractmethod

class Comando(ABC):
    def __init__(self):
        self.receptor = None

    @abstractmethod
    def ejecutar(self, alguien=None):
        pass
