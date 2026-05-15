from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from laberinto_factory import LaberintoFactory

class Juego:
    def __init__(self, factory=None):
        self.factory = factory or LaberintoFactory()
        self.prototipo = None
        self.laberinto = None
        self.bichos = []
        self.personaje = None

    def notificar(self, remitente, evento, datos=None):
        """Método de mediación central (Patrón Mediator)"""
        if evento == "atacar":
            objetivo = datos
            print(f"JUEGO (Mediador): {remitente.nombre if hasattr(remitente, 'nombre') else remitente.__class__.__name__} ataca a {objetivo.nombre if hasattr(objetivo, 'nombre') else objetivo.__class__.__name__} con {remitente.poder} puntos de poder.")
            objetivo.recibir_dano(remitente.poder)
        elif evento == "derrotado":
            print(f"JUEGO (Mediador): Certificado de defunción emitido para {remitente.nombre if hasattr(remitente, 'nombre') else remitente.__class__.__name__}.")
        elif evento == "entrar_habitacion":
            habitacion = datos
            print(f"JUEGO (Mediador): Sistema centralizado detecta movimiento hacia la habitación {habitacion.num}.")
            
            from personaje import Personaje
            from bicho import Bicho
            if isinstance(remitente, Personaje):
                for bicho in list(self.bichos):
                    if bicho.posicion == habitacion and bicho.esta_vivo():
                        print(f" ¡EMBOSCADA! {remitente.nombre} se topa con un {bicho.__class__.__name__} en la habitación {habitacion.num}.")
                        while remitente.esta_vivo() and bicho.esta_vivo():
                            remitente.atacar(bicho)
                            if bicho.esta_vivo():
                                bicho.atacar(remitente)
                                
            elif isinstance(remitente, Bicho):
                if hasattr(self, 'personaje') and self.personaje and self.personaje.posicion == habitacion:
                    if self.personaje.esta_vivo() and remitente.esta_vivo():
                        print(f" ¡EMBOSCADA! Un {remitente.__class__.__name__} ha sorprendido a {self.personaje.nombre} en la habitación {habitacion.num}.")
                        while remitente.esta_vivo() and self.personaje.esta_vivo():
                            remitente.atacar(self.personaje)
                            if self.personaje.esta_vivo():
                                self.personaje.atacar(remitente)

    def clonar_laberinto(self):
        """Patrón Prototype: Devuelve un clon del prototipo guardado"""
        return self.prototipo.clonar() if self.prototipo else None

    def fabricar_laberinto(self):
        return self.factory.fabricar_laberinto()

    def fabricar_habitacion(self, numero):
        return self.factory.fabricar_habitacion(numero)

    def fabricar_pared(self):
        return self.factory.fabricar_pared()

    def fabricar_puerta(self, lado1=None, lado2=None):
        return self.factory.fabricar_puerta(lado1, lado2)

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def obtener_habitacion(self, numero):
        if self.laberinto is None:
            return None
        return self.laberinto.obtener_habitacion(numero)

    def crear_laberinto_demo(self):
        laberinto = self.fabricar_laberinto()

        habitacion_1 = self.fabricar_habitacion(1)
        habitacion_2 = self.fabricar_habitacion(2)

        puerta = self.fabricar_puerta(habitacion_1, habitacion_2)

        habitacion_1.poner_en(Norte(), self.fabricar_pared())
        habitacion_1.poner_en(Sur(), self.fabricar_pared())
        habitacion_1.poner_en(Oeste(), self.fabricar_pared())
        habitacion_1.poner_en(Este(), puerta)

        habitacion_2.poner_en(Norte(), self.fabricar_pared())
        habitacion_2.poner_en(Sur(), self.fabricar_pared())
        habitacion_2.poner_en(Este(), self.fabricar_pared())
        habitacion_2.poner_en(Oeste(), puerta)


        laberinto.agregar_habitacion(habitacion_1)
        laberinto.agregar_habitacion(habitacion_2)

        self.prototipo = laberinto
        self.laberinto = self.clonar_laberinto()
        return self.laberinto