from abc import ABC, abstractmethod

class Orientacion(ABC):
    @abstractmethod
    def poner_en(self, contenedor, elemento):
        pass

    @abstractmethod
    def obtener_de(self, contenedor):
        pass
