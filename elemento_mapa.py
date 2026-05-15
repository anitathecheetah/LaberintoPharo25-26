class ElementoMapa:
    def __init__(self):
        self.padre = None
        self.comandos = []

    def agregar_comando(self, comando):
        self.comandos.append(comando)

    def entrar(self, alguien=None):
        raise NotImplementedError("Este metodo debe redefinirse")

    def recorrer(self, bloque):
        if callable(bloque):
            bloque(self)

    def aceptar(self, visitor):
        pass
