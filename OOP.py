from abc import ABC, abstractmethod

#creo mi intefaz
class comunicacion(ABC):
    @abstractmethod
    def comunicar(self, mesaje):
        pass

#Clase base Vehiculo
