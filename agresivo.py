from modo import Modo


class Agresivo(Modo):
    def actuar(self, bicho):
        print(f"El bicho reacciona con agresividad y ataca con poder {bicho.poder}")