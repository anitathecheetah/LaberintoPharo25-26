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
        
    def notificar(self, evento, datos=None):
        if self.juego:
            self.juego.notificar(self, evento, datos)
            
    def esta_vivo(self):
        return self.vidas > 0
        
    def recibir_dano(self, cantidad):
        self.vidas -= cantidad
        print(f"[{self.__class__.__name__}] Ouch! Recibe {cantidad} de daño. Vidas: {self.vidas}")
        if not self.esta_vivo():
            print(f"[{self.__class__.__name__}]  Ha sido derrotado.")
            self.notificar("derrotado")
            
    def atacar(self, objetivo):
        # En vez de pegarle directamente, avisa al mediador (Juego)
        self.notificar("atacar", objetivo)

    def moverse_a(self, habitacion):
        self.posicion = habitacion
        self.notificar("entrar_habitacion", habitacion)
