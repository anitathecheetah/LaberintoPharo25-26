from abc import ABC, abstractmethod

class Forma(ABC):
    """
    Implementor en el patrón Bridge. 
    Define la interfaz base para las formas geométricas de los contenedores.
    """
    @abstractmethod
    def obtener_orientaciones(self):
        pass
    
    @abstractmethod
    def obtener_nombre(self):
        pass
    
    @abstractmethod
    def num_orientaciones(self):
        pass
    
    def __str__(self):
        return self.obtener_nombre()
