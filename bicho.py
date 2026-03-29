class Bicho:
    def __init__(self, modo, vidas=100, poder=10):
        self.modo = modo
        self.vidas = vidas
        self.poder = poder
        self.posicion = None

    def actuar(self):
        self.modo.actuar(self)

    def cambiar_modo(self, nuevo_modo):
        self.modo = nuevo_modo