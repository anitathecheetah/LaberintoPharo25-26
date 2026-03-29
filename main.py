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

    print("\n--- Probando Factory Method con JuegoBomba y Decorator ---")
    juego_bomba = JuegoBomba()
    laberinto_bomba = juego_bomba.crear_laberinto_demo()
    habitacion_bomba = laberinto_bomba.habitaciones[0]
    print("Probando el norte (esperando pared decorada con bomba):")
    habitacion_bomba.norte.activa = True
    habitacion_bomba.norte.entrar()

    print("\n--- Probando Decorator Dinámico (Hechizo) ---")
    from hechizo import Hechizo
    print("Decorando la puerta este actual con un Hechizo:")
    habitacion_bomba.este = Hechizo(habitacion_bomba.este)
    habitacion_bomba.este.entrar()

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

    print("\n--- Probando Builder y Director ---")
    from director import Director
    director = Director()
    try:
        juego_construido = director.procesar("laberintos/lab2hab2b.json")
        lab_builder = juego_construido.laberinto
        print(f"Builder y Director han ensamblado con éxito un laberinto con {len(lab_builder.habitaciones)} habitaciones desde JSON.")
    except Exception as e:
        print(f"Error probando Builder: {e}")
    print("\n--- Probando Singleton en Orientaciones ---")
    from norte import Norte as ImportNorte
    n1 = ImportNorte()
    n2 = ImportNorte()
    print(f"¿Son n1 y n2 la misma y única instancia en memoria? {'Sí' if n1 is n2 else 'No'}")

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

    print("\n--- Probando Proxy (Tunel) ---")
    from tunel import Tunel
    juego_proxy = Juego()
    laberinto_proxy = juego_proxy.crear_laberinto_demo()
    
    tunel = Tunel(laberinto_proxy)
    from norte import Norte as ImportNorteProxy
    print("Colocando el Túnel Mágico en el Norte de la habitacion_1:")
    habitacion_1.poner_en(ImportNorteProxy(), tunel)
    
    print("Entras en el túnel:")
    habitacion_1.norte.entrar()
    
    print("El bicho te persigue por el túnel:")
    habitacion_1.norte.entrar(bicho)
    
    print("\n--- Probando Adapter (Varita Mágica) ---")
    from personaje import Personaje
    from bicho_adapter import BichoAdapter
    
    aventurero = Personaje("Ana (La bruja piruja)")
    print(f"Estado inicial del bicho: {bicho.modo.__class__.__name__}")
    
    # Creamos un adaptador para que el héroe pueda usar el bicho como si fuera una Varita
    varita_magica = BichoAdapter(bicho)
    aventurero.usar_varita(varita_magica)
    print(f"Estado tras el primer ataque: {bicho.modo.__class__.__name__}")
    
    print("\nUsando la varita de nuevo para revertirlo...")
    aventurero.usar_varita(varita_magica)
    print(f"Estado tras el segundo ataque: {bicho.modo.__class__.__name__}")

    print("\n--- Probando Mediator (Juego centralizando interacciones) ---")
    # Enlazamos los entes con el mediador (Juego)
    aventurero.juego = juego
    bicho.juego = juego
    
    print("El aventurero decide atacar al bicho. Petición enviada al Mediator:")
    aventurero.atacar(bicho)
    
    print("El bicho furioso contraataca pidiendo permiso al Mediator:")
    # Como bicho usa el modo, el modo ataque delega o llamamos directamente atacar
    bicho.atacar(aventurero)
    
    print("Ataque letal del aventurero para ver la notificación de muerte:")
    aventurero.poder = 1000  # Truco de fuerza
    aventurero.atacar(bicho)


if __name__ == "__main__":
    main()