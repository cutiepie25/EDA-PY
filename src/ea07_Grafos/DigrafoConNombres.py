from algs4.digraph import Digraph
from typing import List

class DigrafoConNombres(Digraph):

    def __init__(self, nodos: List[str], **kwargs):
        super().__init__(len(nodos), **kwargs)
        self._nombres = dict()
        self._numeros = dict()
        for i,n in enumerate(nodos):
            self._nombres[n] = i
            self._numeros[i] = n

    def add_edge(self, a: str, b: str):
        u = self._nombres[a]
        v = self._nombres[b]
        super().add_edge(v,u)

    # TODO Ejercicio 1: Obtener la lista de "nombres" adyacentes 
    def adj(self, node: str) -> List[str]:
        pass

    # TODO Ejercicio 2: Obtener el grado entrante del "nodo" v
    def indegree(self, v: str) -> int:
        pass

    # TODO Ejercicio 3: Obtener el grado saliente del "nodo" v
    def outdegree(self, v: str) -> int:
        pass

    # TODO Ejercicio 4: Obtener una representacion textual del grafo usando los nombres
    def __str__(self) -> str:
        s = f'{self.V} vertices, {self.E} edges'
        return s


if __name__ == "__main__":
    g = DigrafoConNombres(["turbo","pasto","pereira","medellin","bogota"])
    g.add_edge('medellin', 'pereira')
    print(g)
