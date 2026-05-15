class Modo:
    def actuar(self, bicho):
        # Este es el Template Method 
        # Define el esqueleto inmutable del algoritmo
        self.caminar(bicho)
        self.atacar(bicho)
        self.dormir(bicho)

    def caminar(self, bicho):
        raise NotImplementedError("Este metodo debe redefinirse")

    def atacar(self, bicho):
        raise NotImplementedError("Este metodo debe redefinirse")

    def dormir(self, bicho):
        raise NotImplementedError("Este metodo debe redefinirse")

    def cambiar_modo(self, bicho):
        raise NotImplementedError("Este metodo debe redefinirse")

