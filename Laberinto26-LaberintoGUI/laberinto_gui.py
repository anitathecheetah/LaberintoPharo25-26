class LaberintoGUI:
    """Interfaz gráfica del laberinto.

    Aquí es un stub pendiente de implementar.
    """

    def __init__(self):
        self.juego = None
        self.person = None
        self.win = None

    def iniciar_juego(self):
        """Carga el laberinto desde JSON y lo muestra."""
        pass  # pendiente de implementar

    def mostrar_laberinto(self):
        """Calcula la posicion y dibuja el laberinto (pendiente de implementar)."""
        self._calcular_posicion()

    def _calcular_posicion(self):
        """Calcula la posicion relativa de las habitaciones respecto de hab1."""
        pass  # pendiente de implementar

    def __str__(self):
        return "LaberintoGUI"
