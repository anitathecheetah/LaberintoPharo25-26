from modo import Modo


class Agresivo(Modo):
    def caminar(self, bicho):
        print(f"El bicho {bicho.__class__.__name__} busca pelea agresivamente.")

    def atacar(self, bicho):
        print(f"El bicho reacciona con agresividad y ataca con poder {bicho.poder * 2}")
        
    def dormir(self, bicho):
        print(f"El bicho apenas duerme, se mantiene en vela y alerta.")
