from dataclasses import dataclass
from Fecha import Fecha

@dataclass(order=True)
class Persona:
    edad: int
    nombre: str
    fechaNacimiento: Fecha


if __name__ == "__main__":
    p1 = Persona(32, "Juan", Fecha(1990,4,20))
    p2 = Persona(27, "Maria", Fecha(1995,9,11))
    p3 = Persona(34, "Laura", Fecha(1988,7,2))

    print(p1)
    print(p2)    
    print(p3)    
    assert p1>p2, "p1 es mayor a p2"
    assert p2<p3, "p2 es menor a p3"
    assert not(p3<p1), "p3 no es menor a p1"