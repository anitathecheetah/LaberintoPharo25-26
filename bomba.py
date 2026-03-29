from decorator import Decorator

class Bomba(Decorator):
    def __init__(self, componente):
        super().__init__(componente)
        self.activa = False

    def entrar(self, alguien=None):
        if self.activa:
            print(f"¡BOOM! La bomba en {type(self.component).__name__} ha explotado.")
        else:
            print(f"Pasas por {type(self.component).__name__} con una bomba inactiva.")
        # Llamar al componente original después (o antes) de la acción del decorador
        super().entrar(alguien)
