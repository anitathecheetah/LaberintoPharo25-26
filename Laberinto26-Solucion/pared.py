from hoja import Hoja


class Pared(Hoja):
    def entrar(self, alguien=None):
        print("Te has chocado con una pared")

    def aceptar(self, visitor):
        visitor.visitar_pared(self)