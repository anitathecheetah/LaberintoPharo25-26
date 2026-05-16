from hoja import Hoja

class Llave(Hoja):
    """
    Extensión Pequeña: Llave para abrir puertas bloqueadas.
    Representa el Cuerno Mágico de Susan.
    """
    def __init__(self, num_p1, num_p2, nombre="Llave Mágica"):
        super().__init__()
        self.num_p1 = num_p1
        self.num_p2 = num_p2
        self.nombre = nombre
        self.encontrada = False

    def entrar(self, alguien):
        from personaje import Personaje
        if isinstance(alguien, Personaje) and not self.encontrada:
            print(f"!!! ¡Has encontrado {self.nombre}! !!!")
            
            # Buscar la puerta dinámicamente en el laberinto clonado
            puerta_objetivo = None
            if hasattr(alguien, 'juego') and alguien.juego:
                hab1 = alguien.juego.obtener_habitacion(self.num_p1)
                hab2 = alguien.juego.obtener_habitacion(self.num_p2)
                if hab1 and hab2:
                    from norte import Norte; from sur import Sur; from este import Este; from oeste import Oeste
                    from puerta import Puerta
                    orientaciones = [Norte(), Sur(), Este(), Oeste()]
                    for ori in orientaciones:
                        elemento = ori.obtener_de(hab1)
                        if isinstance(elemento, Puerta) and (elemento.lado2 == hab2 or elemento.lado1 == hab2):
                            puerta_objetivo = elemento
                            break

            if puerta_objetivo:
                from estado_puerta import Cerrada
                puerta_objetivo.estado = Cerrada()
                print(f"A lo lejos, escuchas el chasquido de la {puerta_objetivo} desbloqueándose.")
                self.encontrada = True
                
                # Notificamos a la Profecía
                if hasattr(alguien, 'juego') and alguien.juego:
                    alguien.juego.notificar_observadores("llave_recogida", self)
            else:
                print(f"La {self.nombre} vibra, pero no encuentra su cerradura.")

    def aceptar_contenedor(self, visitor):
        pass
