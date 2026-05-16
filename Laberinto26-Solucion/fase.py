from abc import ABC, abstractmethod

class Fase(ABC):
    """
    Patrón State: Interfaz para las fases del Juego.
    """
    def __init__(self, juego):
        self.juego = juego

    @abstractmethod
    def entrar_habitacion(self, remitente, habitacion):
        pass

    @abstractmethod
    def personaje_derrotado(self):
        pass

    @abstractmethod
    def enemigo_derrotado(self, enemigo):
        pass

    @abstractmethod
    def personaje_gana(self):
        pass

class Inicial(Fase):
    """Fase inicial antes de que comience la acción."""
    def entrar_habitacion(self, remitente, habitacion):
        print("JUEGO: Transición de fase Inicial -> Jugando")
        self.juego.fase = Jugando(self.juego)
        self.juego.fase.entrar_habitacion(remitente, habitacion)

    def personaje_derrotado(self):
        pass

    def enemigo_derrotado(self, enemigo):
        pass

    def personaje_gana(self):
        pass

class Jugando(Fase):
    """Fase principal donde ocurre el juego."""
    def entrar_habitacion(self, remitente, habitacion):
        print(f"JUEGO (Fase Jugando): Sistema detecta movimiento hacia la habitación {habitacion.num}.")
        
        from personaje import Personaje
        from bicho import Bicho
        from armario import Armario
        
        # Lógica de combate
        for bicho in list(self.juego.bichos):
            if bicho.posicion == habitacion and bicho.esta_vivo():
                print(f" ¡EMBOSCADA! {remitente.nombre if hasattr(remitente, 'nombre') else 'El personaje'} se topa con un {bicho.__class__.__name__} ({bicho.nombre if hasattr(bicho, 'nombre') else ''}) en la habitación {habitacion.num}.")
                while remitente.esta_vivo() and bicho.esta_vivo():
                    remitente.atacar(bicho)
                    if bicho.esta_vivo():
                        bicho.atacar(remitente)
                        
        if isinstance(remitente, Bicho):
            if hasattr(self.juego, 'personaje') and self.juego.personaje and self.juego.personaje.posicion == habitacion:
                if self.juego.personaje.esta_vivo() and remitente.esta_vivo():
                    print(f" ¡EMBOSCADA! Un {remitente.__class__.__name__} ({remitente.nombre if hasattr(remitente, 'nombre') else ''}) ha sorprendido al personaje en la habitación {habitacion.num}.")
                    while remitente.esta_vivo() and self.juego.personaje.esta_vivo():
                        remitente.atacar(self.juego.personaje)
                        if self.juego.personaje.esta_vivo():
                            self.juego.personaje.atacar(remitente)

    def personaje_derrotado(self):
        print("JUEGO: Transición de fase Jugando -> Final (Derrota)")
        self.juego.fase = Final(self.juego, "Has Muerto")

    def enemigo_derrotado(self, enemigo):
        nombre = enemigo.nombre if hasattr(enemigo, 'nombre') else ''
        if "Bruja Blanca" in nombre:
            print(f"¡Has derrotado a la {nombre}!")
            self.personaje_gana()

    def personaje_gana(self):
        print("JUEGO: Transición de fase Jugando -> Final (Victoria)")
        self.juego.fase = Final(self.juego, "¡Has matado a la Bruja Blanca! Sales del armario y te reencuentras con tu familia en Narnia. ¡Has Ganado!")

class Final(Fase):
    """Fase de fin de juego."""
    def __init__(self, juego, resultado=""):
        super().__init__(juego)
        self.resultado = resultado
        print(f"--- FIN DEL JUEGO: {self.resultado} ---")

    def entrar_habitacion(self, remitente, habitacion):
        print(f"JUEGO (Fase Final): El juego ha terminado ({self.resultado}). No se registran más movimientos.")

    def personaje_derrotado(self):
        pass

    def enemigo_derrotado(self, enemigo):
        pass

    def personaje_gana(self):
        pass
