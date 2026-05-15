from elemento_mapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self, forma=None):
        super().__init__()
        self.hijos = []
        self.forma = forma

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def recorrer_hijos(self):
        return iter(self.hijos)

    def recorrer(self, bloque):
        super().recorrer(bloque)
        for hijo in self.hijos:
            hijo.recorrer(bloque)

    def aceptar(self, visitor):
        self.aceptar_contenedor(visitor)
        for hijo in self.hijos:
            hijo.aceptar(visitor)

    def aceptar_contenedor(self, visitor):
        pass