from habitacion import Habitacion

class HabitacionTrampa(Habitacion):
    """
    Extensión Pequeña: Una habitación que daña al personaje automáticamente al entrar.
    Representa el "Invierno Eterno" de la Bruja Blanca.
    """
    def __init__(self, num, dano=5):
        super().__init__(num)
        self.dano = dano

    def entrar(self, alguien):
        from personaje import Personaje
        if isinstance(alguien, Personaje):
            print(f"*** ¡Sientes un frío gélido! El Invierno Eterno te congela. Recibes {self.dano} de daño. ***")
            alguien.recibir_dano(self.dano)
            if not alguien.esta_vivo():
                return  # Si muere por el frío, no sigue explorando
                
        # Llamar a super().entrar() para explorar armarios y demás hijos de la habitación
        super().entrar(alguien)
