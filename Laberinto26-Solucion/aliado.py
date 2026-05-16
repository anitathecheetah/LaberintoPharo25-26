from hoja import Hoja
from manejador_dano import ManejadorDano

class Aliado(Hoja, ManejadorDano):
    """
    Representa a un NPC aliado (ej. Aslan) que se puede encontrar en el laberinto.
    Actúa como un ManejadorDano (Chain of Responsibility) que intercepta el daño
    para proteger al Personaje, sacrificándose si es necesario.
    """
    def __init__(self, nombre="Aliado", escudo=1000):
        Hoja.__init__(self)
        ManejadorDano.__init__(self)
        self.nombre = nombre
        self.escudo = escudo
        self.encontrado = False

    def entrar(self, alguien):
        from personaje import Personaje
        if isinstance(alguien, Personaje) and not self.encontrado:
            print(f"!!! Has encontrado a tu poderoso aliado: {self.nombre} 🦁 !!!")
            print(f"--> {self.nombre} te protegerá en la batalla final.")
            alguien.equipar_defensa(self)
            self.encontrado = True
            if hasattr(alguien, 'juego') and alguien.juego:
                alguien.juego.notificar_observadores("aliado_equipado", self)

    def gestionar_dano(self, cantidad):
        if self.escudo > 0:
            dano_bloqueado = min(cantidad, self.escudo)
            self.escudo -= dano_bloqueado
            cantidad_restante = cantidad - dano_bloqueado
            
            print(f"[{self.nombre}] se interpone heroicamente y bloquea {dano_bloqueado} de daño!")
            
            if self.escudo <= 0:
                print(f"[{self.nombre}] ha recibido una herida mortal y se ha sacrificado para salvarte... T_T")
                from estado_ente import Muerto
                self.estado = Muerto()
                
            if cantidad_restante > 0 and self.sucesor is not None:
                return self.sucesor.gestionar_dano(cantidad_restante)
            else:
                return cantidad_restante
        elif self.sucesor is not None:
            return self.sucesor.gestionar_dano(cantidad)
        else:
            return cantidad
