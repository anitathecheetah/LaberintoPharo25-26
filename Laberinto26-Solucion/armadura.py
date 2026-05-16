from hoja import Hoja
from manejador_dano import ManejadorDano

class Armadura(Hoja, ManejadorDano):
    """
    Patrón Chain of Responsibility: ConcreteHandler.
    Es también un ElementoMapa (Hoja) para poder estar en la habitación.
    """
    def __init__(self, nombre, defensa):
        Hoja.__init__(self)
        ManejadorDano.__init__(self)
        self.nombre = nombre
        self.defensa_maxima = defensa
        self.defensa_actual = defensa

    def gestionar_dano(self, cantidad):
        if self.defensa_actual > 0:
            dano_bloqueado = min(cantidad, self.defensa_actual)
            self.defensa_actual -= dano_bloqueado
            cantidad_restante = cantidad - dano_bloqueado
            print(f"[{self.nombre}] absorbe {dano_bloqueado} de daño. (Durabilidad restante: {self.defensa_actual})")
            
            if cantidad_restante > 0 and self.sucesor is not None:
                return self.sucesor.gestionar_dano(cantidad_restante)
            else:
                return cantidad_restante
        elif self.sucesor is not None:
            return self.sucesor.gestionar_dano(cantidad)
        else:
            return cantidad

    def entrar(self, alguien=None):
        if not getattr(self, 'equipada', False) and alguien is not None and hasattr(alguien, 'equipar_defensa'):
            print(f"{alguien.__class__.__name__} encuentra una armadura: {self.nombre} (+{self.defensa_maxima} DEF)")
            alguien.equipar_defensa(self)
            self.equipada = True
            
    def aceptar(self, visitor):
        if hasattr(visitor, 'visitar_armadura'):
            visitor.visitar_armadura(self)
        elif hasattr(visitor, 'visitar_hoja'):
            visitor.visitar_hoja(self)
