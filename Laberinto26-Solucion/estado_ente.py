from abc import ABC, abstractmethod

class EstadoEnte(ABC):
    """
    Patrón State: Interfaz para los estados de un Ente.
    """
    @abstractmethod
    def esta_vivo(self) -> bool:
        pass

    @abstractmethod
    def atacar(self, ente, objetivo):
        pass

class Vivo(EstadoEnte):
    """
    Estado concreto: El ente está vivo y puede realizar acciones.
    """
    def esta_vivo(self) -> bool:
        return True

    def atacar(self, ente, objetivo):
        # El ente ataca usando el mediador
        ente.notificar("atacar", objetivo)

class Muerto(EstadoEnte):
    """
    Estado concreto: El ente está muerto y no puede interactuar o ser objetivo válido de algunas cosas.
    """
    def esta_vivo(self) -> bool:
        return False

    def atacar(self, ente, objetivo):
        print(f"[{ente.nombre if hasattr(ente, 'nombre') else ente.__class__.__name__}] está muerto y no puede atacar.")
