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
        from fase import Inicial
        self.fase = Inicial(self)
        self.observadores = []

    def agregar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar_observadores(self, evento, datos=None):
        """Patrón Observer: Notifica a los observadores externos de eventos importantes."""
        for obs in self.observadores:
            obs.actualizar(evento, datos)

    def notificar(self, remitente, evento, datos=None):
        """Método de mediación central (Patrón Mediator)"""
        if evento == "atacar":
            objetivo = datos
            poder_real = remitente.poder
            from bicho import Bicho
            if isinstance(remitente, Bicho) and hasattr(remitente, 'modo') and remitente.modo:
                from perezoso import Perezoso
                if isinstance(remitente.modo, Perezoso):
                    poder_real = remitente.poder // 2
                    print(f"JUEGO (Mediador): {remitente.nombre if hasattr(remitente, 'nombre') else remitente.__class__.__name__} está apaciguado (Perezoso). Su ataque se reduce a {poder_real}.")
            print(f"JUEGO (Mediador): {remitente.nombre if hasattr(remitente, 'nombre') else remitente.__class__.__name__} ataca a {objetivo.nombre if hasattr(objetivo, 'nombre') else objetivo.__class__.__name__} con {poder_real} puntos de poder.")
            objetivo.recibir_dano(poder_real)
        elif evento == "derrotado":
            print(f"JUEGO (Mediador): Certificado de defunción emitido para {remitente.nombre if hasattr(remitente, 'nombre') else remitente.__class__.__name__}.")
            self.notificar_observadores("enemigo_derrotado", remitente)
            from personaje import Personaje
            from bicho import Bicho
            if isinstance(remitente, Personaje):
                self.fase.personaje_derrotado()
            elif isinstance(remitente, Bicho):
                if hasattr(self.fase, 'enemigo_derrotado'):
                    self.fase.enemigo_derrotado(remitente)
        elif evento == "entrar_habitacion":
            habitacion = datos
            self.fase.entrar_habitacion(remitente, habitacion)

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
        bicho.juego = self
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