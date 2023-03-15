

class Nodo:
    """Representacion de nodos de la lista simplemente enlazada
    
    Atributos
    ---------
    _item : Dato almacenado en el nodo
    _next : Referencia al siguiente nodo de la lista    
    """

    def __init__(self, item, next: 'Nodo'):
        """Constructor de nodo, acepta un item y el nodo siguiente"""
        self._item = item
        self._next = next


class ListaSimple:
    """Clase que representa una lista simplemente enlazada.
    
    Atributos
    ---------
    _head : La cabeza de la lista.
    _n : Numero de elementos

    Metodos
    -------
    add : Agrega un item a la lista.
    __iter__ : Devolver el iterador de la lista
    __next__ : Obtener el siguiente elemento del iterador

    """

    def __init__(self):
        """Constructor de la lista simple, inicializada como lista vacia"""
        self._head = None
        self._n = 0

    def add(self, item):
        """Agregar un item en la lista simple"""
        self._head = Nodo(item, self._head)
        self._n += 1

    def isEmpty(self) -> bool:
        """Retorna true si la lista esta vacia"""
        return self._n == 0
    
    def size(self) -> int:
        """Retorna el numero de elementos en la lista"""
        return self._n

    def __iter__(self):
        """Obtener el iterador de la lista simple"""
        self._current = self._head
        return self

    def __next__(self):
        """Obtener el siguiente item del iterador"""
        if self._current is not None:
            item = self._current._item
            self._current = self._current._next
            return item
        else:
            raise StopIteration

    def removeHead(self):
        """Borra el primer nodo de la lista"""
        # TODO : Implementar
        pass

    def removeLast(self):
        """Borra el ultimo nodo de la lista"""
        # TODO : Implementar
        pass

    def addLast(self, item):
        """Agrega un item al final de la lista"""
        # TODO : Implementar
        pass

    def get(self, i:int):
        """Retorna el item en la posicion i de la lista"""
        # TODO : Implementar
        pass

    def insert(self, i:int, item):
        """Inserta un item en la posicion i de la lista"""
        # TODO : Implementar
        pass

    def remove(self, i:int):
        """Remueve el nodo de la posicion i de la lista"""
        # TODO : Implementar
        pass

    def invert(self):
        """Devuelve una nueva lista con los elementos originales en orden inverso"""
        # TODO : Implementar
        pass


if __name__ == "__main__":
    l = ListaSimple()
    l.add(1)
    l.add(2)
    l.add(3)

    for i in l:
        print(i)

