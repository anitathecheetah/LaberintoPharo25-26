from modo import Modo


class Perezoso(Modo):
    def caminar(self, bicho):
        print(f"El bicho {bicho.__class__.__name__} se mueve con parsimonia casi sin avanzar.")
        
    def atacar(self, bicho):
        print(f"El bicho ignora el combate y responde con apatía poder {bicho.poder // 2}")

    def dormir(self, bicho):
        print(f"El bicho cae en un profundo y largo sueño.")
