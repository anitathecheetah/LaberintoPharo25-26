from abc import ABC, abstractmethod

class ManejadorDano(ABC):
    """
    Patrón Chain of Responsibility: Handler.
    Define la interfaz para manejar peticiones de daño.
    """
    def __init__(self):
        self.sucesor = None

    def set_sucesor(self, sucesor):
        self.sucesor = sucesor
        return self.sucesor # Permite encadenar

    @abstractmethod
    def gestionar_dano(self, cantidad):
        pass
