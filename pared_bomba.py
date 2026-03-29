from pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self, alguien=None):
        if self.activa:
            print("¡BOOM! Has chocado con una pared bomba activa.")
        else:
            print("Has chocado con una pared bomba (inactiva).")
