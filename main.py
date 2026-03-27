from juego import Juego
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso


def main():
    juego = Juego()
    laberinto = juego.crear_laberinto_demo()

    print(f"Laberinto creado con {len(laberinto.habitaciones)} habitaciones")

    habitacion_1 = laberinto.habitaciones[0]
    habitacion_1.mostrar_orientaciones()

    print("\nProbando el norte:")
    habitacion_1.norte.entrar()

    print("\nProbando el este:")
    habitacion_1.este.entrar()

    habitacion_1.este.abierta = True
    print("\nAbriendo la puerta y probando otra vez:")
    habitacion_1.este.entrar()

    print("\n--- Probando Strategy con bichos ---")
    bicho = Bicho(Agresivo(), vidas=120, poder=25)
    bicho.actuar()

    bicho.cambiar_modo(Perezoso())
    bicho.actuar()


if __name__ == "__main__":
    main()