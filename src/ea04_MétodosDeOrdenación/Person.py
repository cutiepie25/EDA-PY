
class Person:

    def __init__(self, nombres:str, apellidos:str, edad:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos} : {self.edad}"

    def __lt__(self, otro: 'Person') -> bool:
        if self.apellidos==otro.apellidos:
            return self.nombres<otro.nombres
        return self.apellidos<otro.apellidos

