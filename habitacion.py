from contenedor import Contenedor


class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self, alguien=None):
        print(f"Has entrado en la habitación {self.num}")

    def ponerEn(self, orientacion, elemento):
        setattr(self, orientacion.lower(), elemento)

    def mostrar_orientaciones(self):
        print("Norte:", type(self.norte).__name__ if self.norte else None)
        print("Sur:", type(self.sur).__name__ if self.sur else None)
        print("Este:", type(self.este).__name__ if self.este else None)
        print("Oeste:", type(self.oeste).__name__ if self.oeste else None)