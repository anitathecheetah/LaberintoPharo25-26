from juego import Juego
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from juego_bomba import JuegoBomba


def main():
    juego = Juego()
    laberinto = juego.crear_laberinto_demo()

    print(f"Laberinto creado con {len(laberinto.habitaciones)} habitaciones")

    habitacion_1 = laberinto.habitaciones[0]
    habitacion_1.mostrar_orientaciones()

    print("\nProbando el norte:")
    habitacion_1.norte.entrar()

    print("\n--- Probando Factory Method con JuegoBomba ---")
    juego_bomba = JuegoBomba()
    laberinto_bomba = juego_bomba.crear_laberinto_demo()
    habitacion_bomba = laberinto_bomba.habitaciones[0]
    print("Probando el norte (esperando pared bomba):")
    habitacion_bomba.norte.activa = True
    habitacion_bomba.norte.entrar()

    print("\n--- Probando Abstract Factory con LaberintoBombasFactory ---")
    from laberinto_bombas_factory import LaberintoBombasFactory
    juego_abstract = Juego(LaberintoBombasFactory())
    laberinto_abstract = juego_abstract.crear_laberinto_demo()
    habitacion_abstract = laberinto_abstract.habitaciones[0]
    print("Probando el norte (esperando pared_bomba directa del Abstract Factory):")
    if hasattr(habitacion_abstract.norte, 'activa'):
        habitacion_abstract.norte.activa = True
    habitacion_abstract.norte.entrar()


    print("\nProbando el este:")
    habitacion_1.este.entrar()

    habitacion_1.este.abierta = True
    print("\nAbriendo la puerta y probando otra vez:")
    habitacion_1.este.entrar()

    print("\n--- Probando Iterator Interno (recorrer) ---")
    elementos_vistos = []
    def contar_elemento(elemento):
        elementos_vistos.append(type(elemento).__name__)
    
    laberinto.recorrer(contar_elemento)
    print(f"El iterador interno ha recorrido {len(elementos_vistos)} elementos en total en el laberinto.")

    print("\n--- Probando Strategy con bichos ---")

    bicho = Bicho(Agresivo(), vidas=120, poder=25)
    bicho.actuar()

    bicho.cambiar_modo(Perezoso())
    bicho.actuar()


if __name__ == "__main__":
    main()