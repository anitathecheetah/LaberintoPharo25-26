class ElementoMapa:
    def __init__(self):
        self.padre = None

    def entrar(self, alguien=None):
        raise NotImplementedError("Este metodo debe redefinirse")

    def recorrer(self, bloque):
        if callable(bloque):
            bloque(self)
