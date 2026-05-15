from varita import Varita

class BichoAdapter(Varita):
    """
    Patrón Adapter: 
    Convierte la interfaz de un Bicho (Adaptee) en la interfaz Varita (Target)
    que espera el Personaje (Client).
    """
    def __init__(self, bicho):
        self.bicho = bicho

    def cambiar_modo(self):
        if self.bicho and hasattr(self.bicho, 'modo') and self.bicho.modo:
            self.bicho.modo.cambiar_modo(self.bicho)
