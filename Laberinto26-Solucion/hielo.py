from decorator import Decorator

class Hielo(Decorator):
    """
    Extensión Pequeña: Decorator que envuelve a un ElementoMapa (como un Armario).
    Al intentar interactuar (entrar) con el elemento, el personaje sufre daño por congelación.
    """
    def __init__(self, componente, dano=5):
        super().__init__(componente)
        self.dano = dano

    def entrar(self, alguien=None):
        from personaje import Personaje
        if isinstance(alguien, Personaje):
            print(f"\n*** ❄️ ¡El armario está congelado! Recibes {self.dano} de daño por el Invierno Eterno. ❄️ ***")
            alguien.recibir_dano(self.dano)
            if not alguien.esta_vivo():
                return
        
        # Después de aplicar el daño, llamamos al componente real (el armario) para que se abra
        super().entrar(alguien)

    def agregarHijo(self, hijo):
        """
        Método puente necesario porque el Decorator (que hereda de ElementoMapa) 
        no tiene agregarHijo. Así permitimos que el JSON pueda meter la llave dentro del armario decorado.
        """
        if hasattr(self.component, 'agregarHijo'):
            self.component.agregarHijo(hijo)
