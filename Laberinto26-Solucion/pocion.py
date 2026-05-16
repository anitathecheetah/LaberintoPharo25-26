from hoja import Hoja

class Pocion(Hoja):
    """
    Extensión Pequeña: Objeto que cura vida al ser recogido.
    Representa el Cordial de Fuego de Lucía.
    """
    def __init__(self, nombre="Poción Curativa", curacion=50):
        super().__init__()
        self.nombre = nombre
        self.curacion = curacion
        self.usada = False

    def entrar(self, alguien):
        from personaje import Personaje
        if isinstance(alguien, Personaje) and not self.usada:
            print(f"*** ¡Has encontrado {self.nombre}! ***")
            alguien.vidas += self.curacion
            print(f"{alguien.nombre} recupera {self.curacion} vidas. (Vidas actuales: {alguien.vidas})")
            self.usada = True
            
            # Notificamos a la Profecía
            if hasattr(alguien, 'juego') and alguien.juego:
                alguien.juego.notificar_observadores("pocion_tomada", self)

    def aceptar_contenedor(self, visitor):
        # Por ahora no es necesario visitarla, pero cumple la interfaz
        pass
