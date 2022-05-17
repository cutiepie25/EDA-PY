from algs4.max_pq import MaxPQ


class Mascota:

    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def getNombre(self) -> str:
        return self._nombre

    def getPeso(self) -> float:
        return self._peso

    def getEdad(self) -> int:
        return self._edad

    def __lt__(self, otra) -> bool:
        return self._peso < otra._peso

    def __str__(self) -> str:
        return f'Mascota: {self._nombre}, peso={self._peso}, edad={self._edad}'


if __name__=="__main__":
    mascotas = [ 
        Mascota("Firulais", 15.3, 2),
        Mascota("Santa's Little Helper", 5.1, 3),
        Mascota("Garfield", 8.4, 5),
        Mascota("Snoopy", 3.8, 4)
    ]
    pqPeso = MaxPQ()
    for m in mascotas:
        pqPeso.insert(m)

    for x in range(pqPeso.size()):
        print(pqPeso.del_max())

    # TODO Como hacer que la cola de prioridad utilice un atributo distinto?
