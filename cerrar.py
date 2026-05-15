from comando import Comando

class Cerrar(Comando):
    def ejecutar(self, alguien=None):
        if self.receptor:
            self.receptor.cerrar()
