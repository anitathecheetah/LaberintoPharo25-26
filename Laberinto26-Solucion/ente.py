from estado_ente import Vivo, Muerto

class Ente:
    """
    Colleague en el patrón Mediator.
    Clase base para Bicho y Personaje. Todos conocen al Juego (Mediator) 
    y se comunican a través de él.
    """
    def __init__(self, vidas=100, poder=10):
        self.vidas = vidas
        self.poder = poder
        self.posicion = None
        self.juego = None
        self.estado = Vivo()
        
    def notificar(self, evento, datos=None):
        if self.juego:
            self.juego.notificar(self, evento, datos)
            
    def esta_vivo(self):
        return self.estado.esta_vivo()
        
    def recibir_dano(self, cantidad):
        if not self.esta_vivo():
            return
            
        self.vidas -= cantidad
        print(f"[{self.__class__.__name__}] Ouch! Recibe {cantidad} de daño. Vidas: {self.vidas}")
        if self.vidas <= 0 and self.esta_vivo():
            self.estado = Muerto()
            print(f"[{self.__class__.__name__}]  Ha sido derrotado.")
            self.notificar("derrotado")
            
    def atacar(self, objetivo):
        self.estado.atacar(self, objetivo)

    def moverse_a(self, habitacion):
        self.posicion = habitacion
        self.notificar("entrar_habitacion", habitacion)
