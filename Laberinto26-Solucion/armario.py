from contenedor import Contenedor

class Armario(Contenedor):
    """
    Representa un armario en el laberinto, que es un contenedor de otros elementos.
    """
    def __init__(self, forma=None):
        super().__init__(forma)

    def entrar(self, alguien=None):
        print("El personaje ha abierto el armario y explorado su interior...")
        # Notificar a los hijos del armario
        for hijo in list(self.hijos):
            if hasattr(hijo, 'entrar'):
                hijo.entrar(alguien)
            
            from bicho import Bicho
            if isinstance(hijo, Bicho):
                # La Bruja sale del armario y entra a la habitación!
                print(f"¡Un {hijo.__class__.__name__} ({getattr(hijo, 'nombre', '')}) ha salido del armario!")
                hijo.posicion = self.padre # la habitación
                if alguien and alguien.juego:
                    alguien.juego.agregar_bicho(hijo)
                self.hijos.remove(hijo)
                
                # Desatar combate inmediatamente si el remitente es el Personaje
                from personaje import Personaje
                if isinstance(alguien, Personaje):
                    while alguien.esta_vivo() and hijo.esta_vivo():
                        alguien.atacar(hijo)
                        if hijo.esta_vivo():
                            hijo.atacar(alguien)

    def aceptar_contenedor(self, visitor):
        if hasattr(visitor, 'visitar_armario'):
            visitor.visitar_armario(self)
