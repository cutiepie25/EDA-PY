"""1. Una aplicación para un parqueadero necesita mantener el número de espacios
disponibles para visualizarlos en la la puerta de entrada. Observar que la
aplicación debe iniciar con el total de espacios y decrementarse cuando entra un
carro hasta que no haya espacios libres. Asi mismo cuando los carros salen se
debe incrementar.
a. Diseñar un ADT para representar el número de espacios. Indicar constructor y
API en forma de una Interface.
b. Escribir un cliente para hacer pruebas unitarias del ADT.
c. Implementar el ADT como una clase de Java."""

from abc import ABC
from abc import abstractmethod
    
class contador_parqueadero (ABC):
    total_espacios : int
    
    @abstractmethod
    def __init__(self, total_espacios):
        ...
    
    @abstractmethod
    def entrar(self):
        ...
    
    @abstractmethod
    def salir(self):
        ...
    
    @abstractmethod
    def get_espacios_disp(self):
        ...
    
class Parqueadero(contador_parqueadero):
    def __init__(self, total_spaces:int) -> None:
        self.total_spaces = total_spaces
        self.espacios_disponibles = total_spaces
        
    def entrada(self):
        if self.espacios_disponibles > 0:
            self.espacios_disponibles -= 1
        else:
            print("No hay espacios disponibles.")
            
    def salida(self):
        if self.espacios_disponibles < self.total_spaces:
            self.espacios_disponibles += 1
        else:
            print("Todos los espacios ya están disponibles.")
        
    def obtener_espacios_disponibles(self) -> int:
        return self.espacios_disponibles
    
