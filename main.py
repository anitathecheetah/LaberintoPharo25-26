from juego import Juego


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


if __name__ == "__main__":
    main()