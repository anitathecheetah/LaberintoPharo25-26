from director import Director


def main():
    director = Director()
    juego = director.procesar("laberintos/lab2hab2b.json")
    laberinto = juego.laberinto

    print(f"Laberinto creado con {len(laberinto.habitaciones)} habitaciones")
    print(f"Bichos creados: {len(laberinto.bichos)}")

    habitacion_1 = laberinto.obtener_habitacion(1)
    habitacion_1.mostrar_orientaciones()

    print("\nProbando la puerta:")
    habitacion_1.este.entrar()

    print("\nProbando bichos:")
    for bicho in laberinto.bichos:
        bicho.actuar()


if __name__ == "__main__":
    main()