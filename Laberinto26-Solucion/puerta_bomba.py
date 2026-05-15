from puerta import Puerta

class PuertaBomba(Puerta):
    def __init__(self, lado1=None, lado2=None):
        super().__init__(lado1, lado2)
        self.activa = False

    def entrar(self, alguien=None):
        if self.activa:
            print("¡BOOM! Has abierto una puerta bomba y ha explotado.")
        else:
            print("La puerta bomba (inactiva) se abre sin problemas.")
            super().entrar(alguien)
