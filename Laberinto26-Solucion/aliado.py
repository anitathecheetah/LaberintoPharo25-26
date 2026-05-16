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
            print(f"!!! Has encontrado a tu poderoso aliado: {self.nombre} !!!")
            print(f"--> {self.nombre} te protegerá en la batalla final.")
            alguien.equipar_defensa(self)
            self.encontrado = True
            if hasattr(alguien, 'juego') and alguien.juego:
                alguien.juego.notificar_observadores("aliado_equipado", self)

    def gestionar_dano(self, cantidad):
        if self.escudo > 0:
            print(f"[{self.nombre}] se interpone heroicamente y recibe el golpe de {cantidad} de daño dirigido a ti!")
            self.escudo -= cantidad
            if self.escudo <= 0:
                print(f"[{self.nombre}] ha recibido una herida mortal y se ha sacrificado para salvarte... 😭")
                from estado_ente import Muerto
                self.estado = Muerto()
            return 0
        else:
            # Si el aliado ya no puede protegerte, el daño pasa al siguiente en la cadena
            return super().gestionar_dano(cantidad)
