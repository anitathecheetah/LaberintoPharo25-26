from abc import ABC, abstractmethod

class Observador(ABC):
    """
    Patrón Observer: Interfaz para los observadores del juego.
    """
    @abstractmethod
    def actualizar(self, evento, datos):
        pass

class ProfeciaNarnia(Observador):
    """
    Observador concreto que narra la aventura en base a los eventos del juego.
    """
    def actualizar(self, evento, datos):
        if evento == "personaje_herido":
            print("\n[PROFESÍA] 'La sangre de los reyes de antaño ha sido derramada...'")
        elif evento == "aliado_equipado":
            nombre_aliado = datos.nombre if hasattr(datos, 'nombre') else 'un amigo'
            print(f"\n[PROFESÍA] 'El gran león está en movimiento... {nombre_aliado} se une a la batalla.'")
        elif evento == "enemigo_derrotado":
            nombre_enemigo = datos.nombre if hasattr(datos, 'nombre') else 'el mal'
            print(f"\n[PROFESÍA] 'Una victoria más. El hielo se resquebraja tras la caída de {nombre_enemigo}.'")
        elif evento == "pocion_tomada":
            print("\n[PROFESÍA] 'El fuego cura el frío de la muerte. Las heridas se cierran.'")
        elif evento == "llave_recogida":
            print("\n[PROFESÍA] 'El sonido de un cuerno antiguo rompe el silencio. Los caminos cerrados se abren.'")
