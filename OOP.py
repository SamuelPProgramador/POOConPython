from abc import ABC, abstractmethod

#creo mi intefaz
class comunicacion(ABC):
    @abstractmethod
    def comunicar(self, mesaje):
        pass

#Clase base Vehiculo
class Vehiculo(comunicacion):
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
    
    def mover(self):
        print(f'EL vehiculo {self.nombre} se mueve a {self.velocidad} km/h')

    
    