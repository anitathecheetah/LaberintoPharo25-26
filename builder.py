from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def fabricarLaberinto(self):
        pass

    @abstractmethod
    def fabricarHabitacion(self, num):
        pass

    @abstractmethod
    def fabricarPuerta(self, lado1, lado2):
        pass

    @abstractmethod
    def fabricarPared(self):
        pass

    @abstractmethod
    def fabricarBichoModo(self, str_modo, posicion):
        pass

    @abstractmethod
    def obtenerLaberinto(self):
        pass