
class Person:

    def __init__(self, nombres:str, apellidos:str, edad:int, peso:float):
        self._nombres = nombres
        self._apellidos = apellidos
        self._edad = edad
        self._peso = peso

    def __str__(self) -> str:
        return f"{self._nombres} {self._apellidos} : {self._edad}, {self._peso:.2f}"

    # TODO: Implementar método __lt__ para comparar personas por apellido y nombre

