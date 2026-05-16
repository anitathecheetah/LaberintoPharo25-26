from ente import Ente
from manejador_dano import ManejadorDano

class Personaje(Ente, ManejadorDano):
    """
    Cliente y final de la cadena en el patrón Chain of Responsibility.
    """
    def __init__(self, nombre="Aventurero", vidas=100, poder=20):
        Ente.__init__(self, vidas, poder)
        ManejadorDano.__init__(self)
        self.nombre = nombre
        self.defensas = self # Inicialmente, la cadena solo es él mismo.

    def gestionar_dano(self, cantidad):
        """Final de la cadena de responsabilidad: El cuerpo recibe el daño restante"""
        self.vidas -= cantidad
        print(f"[{self.__class__.__name__}] Ouch! Recibe {cantidad} de daño real. Vidas: {self.vidas}")
        if hasattr(self, 'juego') and self.juego:
            self.juego.notificar_observadores("personaje_herido", self)
        from estado_ente import Muerto
        if self.vidas <= 0 and self.esta_vivo():
            self.estado = Muerto()
            print(f"[{self.__class__.__name__}]  Ha sido derrotado.")
            self.notificar("derrotado")
        return 0

    def recibir_dano(self, cantidad):
        """Sobrescribe Ente.recibir_dano para pasar la petición por la cadena"""
        self.defensas.gestionar_dano(cantidad)

    def equipar_defensa(self, nueva_defensa):
        """Añade una armadura al principio de la cadena"""
        nueva_defensa.set_sucesor(self.defensas)
        self.defensas = nueva_defensa
        print(f"{self.nombre} se ha equipado: {nueva_defensa.nombre}")

    def usar_varita(self, varita):
        print(f"{self.nombre} agita la varita mágica apuntando al enemigo...")
        varita.cambiar_modo()
