import sys
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from director import Director
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from puerta import Puerta
from pared import Pared
from fase import Final

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def procesar_orientacion(personaje, orientacion):
    hab = personaje.posicion
    elem = orientacion.obtener_de(hab)
    
    if isinstance(elem, Pared):
        print("¡Chocas contra una pared! 🤕")
    elif isinstance(elem, Puerta):
        if elem.esta_cerrada() or str(elem.estado) == "Bloqueada":
            print(f"La puerta hacia el {orientacion.__class__.__name__} está {elem.estado}.")
            if str(elem.estado) == "Bloqueada":
                print("Necesitas la llave (Cuerno Mágico) para desbloquearla.")
            else:
                respuesta = input("¿Quieres abrirla y cruzar? (s/n): ").strip().lower()
                if respuesta == 's':
                    elem.abrir()
                    print(f"¡Has abierto la puerta!")
                    nueva_hab = elem.lado2 if hab == elem.lado1 else elem.lado1
                    elem.entrar(personaje)
                    personaje.moverse_a(nueva_hab)
                else:
                    print("Te quedas donde estás.")
        else:
            nueva_hab = elem.lado2 if hab == elem.lado1 else elem.lado1
            elem.entrar(personaje)
            personaje.moverse_a(nueva_hab)
    else:
        print("Caminas por el pasillo vacío...")

def obtener_nombres_defensas(defensa):
    if defensa is None:
        return "Ninguna"
    nombres = []
    actual = defensa
    while actual is not None:
        if hasattr(actual, 'escudo'):
            nombres.append(f"{actual.nombre} ({actual.escudo})")
        elif hasattr(actual, 'defensa_actual'):
            nombres.append(f"{actual.nombre} ({actual.defensa_actual})")
        else:
            nombres.append(actual.nombre)
        actual = getattr(actual, 'sucesor', None)
    return " + ".join(nombres)

def jugar():
    director = Director()
    juego = director.procesar("laberintos/lab_narnia_3x3.json")
    personaje = juego.personaje

    orientaciones = {
        "w": Norte(),
        "s": Sur(),
        "d": Este(),
        "a": Oeste()
    }

    while not isinstance(juego.fase, Final):
        limpiar_pantalla()
        hab = personaje.posicion
        
        print("=" * 60)
        print("🦁 LAS CRONICAS DE NARNIA: EL INVIERNO ETERNO ❄️")
        print("=" * 60)
        print(f"\n📍 Estas en la habitacion {hab.num}")
        print(f"❤️ Vidas: {personaje.vidas}")
        print(f"🛡️ Defensa: {obtener_nombres_defensas(personaje.defensas)}\n")
        
        print("A tu alrededor ves:")
        for key, ori in orientaciones.items():
            elem = ori.obtener_de(hab)
            if isinstance(elem, Pared):
                estado = "Pared 🧱"
            elif isinstance(elem, Puerta):
                estado = f"Puerta [{elem.estado}] 🚪"
            else:
                estado = "Pasillo"
            
            indicador = {"w": "Norte ↑ (w)", "s": "Sur   ↓ (s)", "d": "Este  → (d)", "a": "Oeste ← (a)"}
            print(f"  - Al {indicador[key]}: {estado}")
        
        print("\n" + "-" * 60)
        print("Controles:")
        print("  Moverse: Escribe 'w', 'a', 's', 'd' y pulsa Enter.")
        print("  Salir: Escribe 'q' y pulsa Enter.")
        
        accion = input("\n¿Qué deseas hacer? ").strip().lower()

        if accion == 'q':
            break
        
        print("\n" + "=" * 60)
        
        if accion in orientaciones:
            procesar_orientacion(personaje, orientaciones[accion])
        else:
            print("Comando no reconocido.")
            
        input("\n[Pulsa Enter para continuar...]")

    limpiar_pantalla()
    if isinstance(juego.fase, Final):
        print("\n" + "=" * 60)
        print("🌟 FIN DEL JUEGO 🌟")
        print(juego.fase.resultado)
        print("=" * 60)
    else:
        print("\nTe has rendido... Narnia seguira bajo el hielo.")

if __name__ == "__main__":
    jugar()
