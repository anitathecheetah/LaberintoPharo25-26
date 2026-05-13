# Laberinto - Patrones de Diseño

Proyecto de la asignatura de Diseño de Software. Consiste en implementar en Python el ejemplo clásico del Laberinto (originalmente en Pharo/Smalltalk), aplicando los patrones de diseño GoF que se han visto en clase.

## Qué hace

El programa modela un laberinto con habitaciones, paredes, puertas y túneles. Dentro del laberinto hay bichos con distintos comportamientos y un personaje que puede interactuar con ellos. Lo importante no es el laberinto en sí, sino cómo se aplican los patrones de diseño para construirlo y extenderlo.

## Cómo ejecutarlo

Solo hace falta Python 3.8 o superior. No tiene dependencias externas.

```bash
python main.py
```

Esto ejecuta una demo que va probando cada patrón uno por uno: crea laberintos, abre puertas, activa bombas, construye desde JSON, etc.

## Patrones implementados

- **Abstract Factory** — `LaberintoFactory` y `LaberintoBombasFactory` crean familias de productos (normal vs. bomba) sin acoplar el cliente a clases concretas.
- **Factory Method** — `Juego` y `JuegoBomba`. Las subclases deciden qué elementos crear.
- **Builder** — `LaberintoBuilder` + `Director`. Construcción paso a paso de laberintos a partir de archivos JSON.
- **Singleton** — `Norte`, `Sur`, `Este`, `Oeste`. Solo existe una instancia de cada orientación.
- **Composite** — `Contenedor` y `Hoja`. El laberinto contiene habitaciones, que contienen paredes/puertas.
- **Decorator** — `Hechizo` y `Bomba` decoran elementos del mapa añadiendo comportamiento extra.
- **Proxy** — `Tunel` actúa como intermediario que teletransporta a otro laberinto.
- **Adapter** — `BichoAdapter` adapta un `Bicho` para que el `Personaje` lo use como si fuera una `Varita`.
- **Strategy** — `Agresivo` y `Perezoso` son estrategias intercambiables que definen cómo actúa un `Bicho`.
- **Iterator** — El método `recorrer()` permite recorrer todos los elementos del laberinto internamente.

## Estructura

```
├── main.py                      # Punto de entrada, ejecuta la demo
├── juego.py / juego_bomba.py    # Factory Method
├── laberinto.py                 # Laberinto (Composite)
├── habitacion.py                # Habitación con 4 lados
├── pared.py / puerta.py         # Elementos básicos del mapa
├── pared_bomba.py / puerta_bomba.py
├── contenedor.py / hoja.py      # Composite base
├── elemento_mapa.py             # Clase abstracta raíz
├── orientacion.py               # Clase base orientación
├── norte.py / sur.py / este.py / oeste.py  # Singleton
├── decorator.py / hechizo.py / bomba.py    # Decorator
├── tunel.py                     # Proxy
├── bicho_adapter.py / varita.py # Adapter
├── personaje.py
├── bicho.py / ente.py           # Entidades
├── modo.py / agresivo.py / perezoso.py  # Strategy
├── builder.py / laberinto_builder.py    # Builder
├── director.py                  # Director
├── laberinto_factory.py         # Abstract Factory
├── laberinto_bombas_factory.py
└── laberintos/                  # JSONs de configuración
    ├── lab2hab2b.json
    └── lab2hab1bic1tun1per.json
```

## Configuración JSON

Se pueden definir laberintos con archivos JSON. El Director los lee y usa el Builder para montarlos. Ejemplo:

```json
{
  "forma": "poligono4",
  "laberinto": [
    { "tipo": "habitacion", "num": 1, "hijos": [] },
    { "tipo": "habitacion", "num": 2, "hijos": [] }
  ],
  "puertas": [
    [1, "Este", 2, "Oeste"]
  ],
  "bichos": [
    { "modo": "Agresivo", "posicion": 1 },
    { "modo": "Perezoso", "posicion": 2 }
  ]
}
```

## Ejemplo de salida

```
Laberinto creado con 2 habitaciones

Probando el norte:
¡Ouch! Te has chocado contra una pared.

--- Probando Factory Method con JuegoBomba y Decorator ---
 ¡BOOM! La bomba explota.

--- Probando Builder y Director ---
Builder y Director han ensamblado con éxito un laberinto con 2 habitaciones desde JSON.

--- Probando Singleton en Orientaciones ---
¿Son n1 y n2 la misma y única instancia en memoria? Sí

--- Probando Strategy con bichos ---
El bicho Bicho busca pelea agresivamente.

--- Probando Proxy (Tunel) ---
--- ! Has entrado en el Túnel Teletransportador (Proxy) ! ---

--- Probando Adapter (Varita Mágica) ---
Un rayo mágico daña al bicho agresivo...
Estado tras el primer ataque: Perezoso
```

## Autora

Ana Rodríguez de Vera Martínez
