from abc import ABC, abstractmethod


class EstadoPuerta(ABC):
    """Interfaz del patron State para el estado de una Puerta."""

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

    @abstractmethod
    def entrar(self, alguien, puerta):
        pass

    def esta_abierta(self):
        return False

    def esta_cerrada(self):
        return False


class Abierta(EstadoPuerta):
    """Estado Abierta de la puerta."""

    def cerrar(self, puerta):
        print(f"Cerramos {puerta}")
        puerta.estado = Cerrada()

    def entrar(self, alguien, puerta):
        puerta.puede_entrar(alguien)

    def esta_abierta(self):
        return True

    def __str__(self):
        return "Abierta"


class Cerrada(EstadoPuerta):
    """Estado Cerrada de la puerta."""

    def abrir(self, puerta):
        print(f"Abrimos {puerta}")
        puerta.estado = Abierta()

    def entrar(self, alguien, puerta):
        print(f"Puerta {puerta} cerrada")

    def esta_cerrada(self):
        return True

    def __str__(self):
        return "Cerrada"
