import sys
import os

_ROOT = os.path.dirname(os.path.abspath(__file__))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder', 'Laberinto26-Visitor', 'Laberinto26-LaberintoGUI']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from director import Director

def main():
    print("---  INICIANDO CONSTRUCCIÓN DESDE JSON COMPLETO ---")
    director = Director()
    juego_construido = director.procesar("laberintos/lab2hab1bic1tun1per.json")
    lab = juego_construido.laberinto
    
    print(f" El Director ha construido un laberinto con {len(lab.habitaciones)} habitaciones principales.")
    
    hab1 = lab.obtener_habitacion(1)
    
    hab2 = lab.obtener_habitacion(2)
    
    # Extraemos a nuestro héroe del Juego
    ana = juego_construido.personaje
    
    print("\n---  Ana avanza a la sala 2... ---")
    ana.moverse_a(hab2) 
    

if __name__ == "__main__":
    main()
