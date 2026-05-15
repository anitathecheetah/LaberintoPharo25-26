from ente import Ente

class Personaje(Ente):
    """
    Cliente (Client) en el patrón Adapter: 
    Solo sabe usar objetos que cumplan la interfaz Varita (Target).
    Y ahora actúa como Colleague del Mediator heredando de Ente.
    """
    def __init__(self, nombre="Aventurero", vidas=100, poder=20):
        super().__init__(vidas, poder)
        self.nombre = nombre

    def usar_varita(self, varita):
        print(f"{self.nombre} agita la varita mágica apuntando al enemigo...")
        varita.cambiar_modo()
