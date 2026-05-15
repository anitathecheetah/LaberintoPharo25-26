from visitor import Visitor

class VisitorAbrirPuertas(Visitor):
    def visitar_puerta(self, puerta):
        puerta.abrir()
