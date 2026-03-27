from hoja import Hoja


class Puerta(Hoja):
    def __init__(self, lado1=None, lado2=None, abierta=False):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = abierta

    def entrar(self, alguien=None):
        if self.abierta:
            print("Has cruzado la puerta")
        else:
            print("La puerta está cerrada")