from modo import Modo


class Perezoso(Modo):
    def actuar(self, bicho):
        print(f"El bicho se mueve con parsimonia y responde con poder {bicho.poder}")