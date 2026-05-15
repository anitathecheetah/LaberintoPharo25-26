from contenedor import Contenedor


class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.habitaciones = []
        self.bichos = []

    def agregar_habitacion(self, habitacion):
        if habitacion is None:
            raise ValueError("La habitacion no puede ser None")
        self.habitaciones.append(habitacion)
        self.agregarHijo(habitacion)

    def obtener_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.num == numero:
                return habitacion
        return None

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def clonar(self):
        """Patrón Prototype: Devuelve una copia profunda del laberinto."""
        import copy
        return copy.deepcopy(self)