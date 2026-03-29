from elemento_mapa import ElementoMapa

class Decorator(ElementoMapa):
    def __init__(self, componente: ElementoMapa):
        self.component = componente

    def entrar(self, alguien=None):
        self.component.entrar(alguien)

    def recorrer(self, bloque):
        if callable(bloque):
            bloque(self)
        self.component.recorrer(bloque)
