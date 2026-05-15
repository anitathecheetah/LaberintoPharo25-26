from ente import Ente

class Bicho(Ente):
    def __init__(self, modo, vidas=100, poder=10):
        super().__init__(vidas, poder)
        self.modo = modo

    def actuar(self):
        self.modo.actuar(self)

    def cambiar_modo(self, nuevo_modo):
        self.modo = nuevo_modo