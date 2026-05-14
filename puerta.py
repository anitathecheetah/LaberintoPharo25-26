from hoja import Hoja
from estado_puerta import Cerrada


class Puerta(Hoja):
    def __init__(self, lado1=None, lado2=None):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.estado = Cerrada()

    def abrir(self):
        self.estado.abrir(self)

    def cerrar(self):
        self.estado.cerrar(self)

    def entrar(self, alguien=None):
        self.estado.entrar(alguien, self)

    def puede_entrar(self, alguien):
        if alguien is None:
            print("Has cruzado la puerta")
            return
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    def esta_abierta(self):
        return self.estado.esta_abierta()

    def esta_cerrada(self):
        return self.estado.esta_cerrada()

    def __str__(self):
        n1 = self.lado1.num if self.lado1 and hasattr(self.lado1, 'num') else "?"
        n2 = self.lado2.num if self.lado2 and hasattr(self.lado2, 'num') else "?"
        return f"Puerta-{n1}-{n2}"