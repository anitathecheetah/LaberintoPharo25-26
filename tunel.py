from hoja import Hoja

class Tunel(Hoja):
    """
    Patrón Proxy: Actúa como intermediario o sustituto para controlar 
    el acceso a un objeto complejo (en este caso, un Laberinto entero).
    """

    def __init__(self, laberinto=None):
        super().__init__()
        self.laberinto = laberinto

    def entrar(self, alguien=None):
        if self.laberinto is None and alguien is not None and hasattr(alguien, 'juego'):
            self.laberinto = alguien.juego.clonar_laberinto()

        if self.laberinto is None:
            print("El túnel parece estar derrumbado. No lleva a ningún sitio.")
            return

        print("--- ! Has entrado en el Túnel Teletransportador (Proxy) ! ---")
        if alguien is not None:
            tipo = alguien.modo.__class__.__name__ if hasattr(alguien, 'modo') else "Aventurero"
            print(f"[{tipo}] {alguien.__class__.__name__} entra en el túnel...")
            print(f"...y es transportado mágicamente a un nuevo Laberinto.")
            # Encontramos la primera habitación del nuevo laberinto para teletransportarnos ahí
            if self.laberinto.habitaciones:
                self.laberinto.habitaciones[0].entrar(alguien)
            else:
                self.laberinto.entrar(alguien)
        else:
            print("Te adentras en el oscuro túnel...")
            print("...y apareces en un lugar completamente distinto.")
            if self.laberinto.habitaciones:
                self.laberinto.habitaciones[0].entrar()
            else:
                self.laberinto.entrar()

    def recorrer(self, bloque):
        """Implementación del Iterator para que atraviese el proxy"""
        bloque(self)
        if self.laberinto is not None:
            self.laberinto.recorrer(bloque)

    def aceptar(self, visitor):
        visitor.visitar_tunel(self)
