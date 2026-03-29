class Personaje:
    """
    Cliente (Client) en el patrón Adapter: 
    Solo sabe usar objetos que cumplan la interfaz Varita (Target).
    """
    def __init__(self, nombre="Aventurero"):
        self.nombre = nombre

    def usar_varita(self, varita):
        print(f"{self.nombre} agita la varita mágica apuntando al enemigo...")
        varita.cambiar_modo()
