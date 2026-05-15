from decorator import Decorator

class Hechizo(Decorator):
    def __init__(self, componente):
        super().__init__(componente)
        self.activo = True

    def entrar(self, alguien=None):
        if self.activo:
            print(f"¡Magia! Un hechizo se activa al entrar en {type(self.component).__name__}.")
        super().entrar(alguien)
