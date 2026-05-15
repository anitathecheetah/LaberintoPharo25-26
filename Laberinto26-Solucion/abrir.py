from comando import Comando

class Abrir(Comando):
    def ejecutar(self, alguien=None):
        if self.receptor:
            self.receptor.abrir()
