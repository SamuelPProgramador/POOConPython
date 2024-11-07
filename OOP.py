

from abc import ABC, abstractmethod

# Interfaz para la comunicación
class Comunicacion(ABC):
    @abstractmethod
    def comunicar(self, mensaje):
        pass

# Clase base Vehiculo
class Vehiculo(Comunicacion):
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
    
    def mover(self):
        print(f"El vehículo {self.nombre} se mueve a {self.velocidad} km/h.")
    
    # Implementación de la comunicación
    def comunicar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

# Clases hijas de Vehiculo
class Coche(Vehiculo):
    def __init__(self, nombre, velocidad, combustible):
        super().__init__(nombre, velocidad)
        self.combustible = combustible

    # Implementación de la comunicación específica de Coche
    def comunicar(self, mensaje):
        print(f"Coche {self.nombre} comunica: {mensaje}")

class Bicicleta(Vehiculo):
    def __init__(self, nombre, velocidad):
        super().__init__(nombre, velocidad)
    
    # Implementación de la comunicación específica de Bicicleta
    def comunicar(self, mensaje):
        print(f"Bicicleta {self.nombre} comunica: {mensaje}")

# Clase base Animal
class Animal(Comunicacion):
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace {self.sonido}.")
    
    # Implementación de la comunicación
    def comunicar(self, mensaje):
        print(f"{self.nombre} responde: {mensaje}")

# Clases hijas de Animal
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "guau")
    
    # Implementación de la comunicación específica de Perro
    def comunicar(self, mensaje):
        print(f"Perro {self.nombre} responde: {mensaje}")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "miau")
    
    # Implementación de la comunicación específica de Gato
    def comunicar(self, mensaje):
        print(f"Gato {self.nombre} responde: {mensaje}")

# Ejemplo de comunicación entre instancias de Vehiculo y Animal
coche = Coche("Toyota", 120, "Gasolina")
perro = Perro("Firulais")

coche.comunicar("Voy en camino.")
perro.comunicar("Estoy listo para el paseo.")
