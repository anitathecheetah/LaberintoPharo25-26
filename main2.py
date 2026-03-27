from builder import Builder


def main():
    builder = Builder()
    builder.fabricar_laberinto()
    builder.fabricar_juego()

    builder.fabricar_habitacion(1)
    builder.fabricar_habitacion(2)
    builder.conectar_habitaciones(1, "este", 2, "oeste")

    builder.fabricar_bicho_modo("agresivo", 1)
    builder.fabricar_bicho_modo("perezoso", 2)

    laberinto = builder.laberinto

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