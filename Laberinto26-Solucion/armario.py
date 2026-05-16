from contenedor import Contenedor

class Armario(Contenedor):
    """
    Representa un armario en el laberinto, que es un contenedor de otros elementos.
    """
    def __init__(self, forma=None):
        super().__init__(forma)

    def entrar(self, alguien=None):
        print("El personaje ha entrado (o abierto) el armario.")
        # Notificar a los hijos del armario
        for hijo in self.hijos:
            hijo.entrar(alguien)

    def aceptar_contenedor(self, visitor):
        if hasattr(visitor, 'visitar_armario'):
            visitor.visitar_armario(self)
