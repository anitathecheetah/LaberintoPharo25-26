from elemento_mapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

    def recorrer_hijos(self):
        return iter(self.hijos)