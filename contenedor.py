from elemento_mapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def recorrer_hijos(self):
        return iter(self.hijos)

    def recorrer(self, bloque):
        super().recorrer(bloque)
        for hijo in self.hijos:
            hijo.recorrer(bloque)