# Laberinto - Narnia & Patrones de Diseño

Este es el proyecto final de la asignatura de Diseño de Software. Consiste en la implementación en Python del clásico juego del Laberinto, aplicando patrones de diseño GoF y ambientándolo temáticamente en "Las Crónicas de Narnia: El Invierno Eterno".

## Qué hace el proyecto

El programa simula un laberinto en consola donde el jugador controla a Peter Pevensie para explorar habitaciones, esquivar trampas de hielo, equipar defensas (armaduras y el aliado Aslan) y derrotar a la Bruja Blanca en el armario de la habitación final. Las interacciones físicas, el combate y los flujos lógicos están gestionados enteramente mediante patrones de diseño.

## Cómo instalarlo o ejecutarlo

### Requisitos
- Python 3.8 o superior.
- No requiere dependencias externas.

### Ejecución del juego interactivo
Para jugar la campaña interactiva en la consola utilizando comandos de teclado (`w`, `a`, `s`, `d`):
```bash
python jugar_narnia.py
```

### Ejecución de la demo base
Para comprobar el funcionamiento secuencial de los patrones del laberinto original:
```bash
python main.py
```

### Ejecución y detalle de los tests unitarios
Para ejecutar el conjunto de 19 pruebas unitarias automatizadas:
```bash
python -m unittest discover -s Laberinto26-Pruebas
```

La suite cuenta con **19 pruebas automatizadas** organizadas en archivos individuales que verifican de forma aislada e independiente cada componente del juego:

- **`test_aliado_chain_responsibility.py` (1 test):** Verifica que el NPC Aslan (Chain of Responsibility) intercepta y mitiga los daños protegiendo al personaje, sacrificándose en caso de daño mortal.
- **`test_profecia_observer.py` (1 test):** Verifica que la `ProfeciaNarnia` (Observer) recibe y procesa reactivamente notificaciones de eventos lanzados por el `Juego`.
- **`test_hielo_decorator.py` (3 tests):** Comprueba que el decorador `Hielo` inflige daño por helada al personaje y que hereda transparentemente la agregación de hijos (`agregarHijo()`).
- **`test_llave_composite.py` (1 test):** Verifica que al recoger la `Llave` (Composite Leaf), esta localiza la puerta asociada en el laberinto y la desbloquea de forma remota.
- **`test_puerta_state.py` (1 test):** Comprueba que una puerta en estado Bloqueada (State) prohíbe el paso hasta ser desbloqueada y pasar al estado Cerrada.
- **`test_pocion_composite.py` (1 test):** Verifica que la `Pocion` (Composite Leaf) incrementa la vida de Peter una única vez.
- **`test_varita_adapter.py` (1 test):** Valida que el `BichoAdapter` (Adapter) transforma el modo de ataque de la Bruja Blanca a `Perezoso` en el último golpe del combate final.
- **`test_chain_responsibility.py` (4 tests):** Verifica que la mitigación de daño de Peter funcione sin equipamiento, con armadura individual, y con múltiples armaduras en cadena.
- **`test_state.py` (5 tests):** Comprueba el control de fases del juego (Inicial, Jugando, Victoria, Derrota) y el cambio de estado de entes de vivo a muerto.
- **`test_narnia.py` (1 test):** Test de integración de la campaña completa de principio a fin, completando la victoria contra la Bruja Blanca.

---

## Patrones implementados

En este proyecto se han implementado y adaptado los siguientes patrones de diseño:

- **Composite:** Habitaciones, armarios, pociones y llaves estructuradas como nodos del mapa.
- **Decorator:** Trampas de helada (`Hielo`) que decoran dinámicamente armarios o habitaciones.
- **State:** Máquina de estados de las puertas (`EstadoPuerta`) con estados Abierta, Cerrada y Bloqueada.
- **Chain of Responsibility:** Sistema de defensas del personaje (`Aliado` y `Armadura`) para interceptar y mitigar el daño en cadena.
- **Observer:** Notificación reactiva de eventos de juego procesada por la clase `ProfeciaNarnia`.
- **Adapter:** `BichoAdapter` que adapta al enemigo Bruja Blanca a la interfaz `Varita` en el combate final.
- **Strategy:** Modos de ataque de los bichos (Agresivo y Perezoso).
- **Singleton:** Representación de orientaciones cardinales (Norte, Sur, Este, Oeste).
- **Builder & Director:** Carga e instanciación dinámica del laberinto a partir del archivo JSON de configuración.
- **Abstract Factory:** `LaberintoFactory` y `LaberintoBombasFactory` para familias de elementos del mapa.
- **Factory Method:** Subclases de `Juego` encargadas de decidir la instanciación de los laberintos.
