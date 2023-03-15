

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

    Metodos
    -------
    add : Agrega un item a la lista.
    __iter__ : Devolver el iterador de la lista
    __next__ : Obtener el siguiente elemento del iterador

    """

    def __init__(self):
        """Constructor de la lista simple, inicializada como lista vacia"""
        self._head = None

    def add(self, item):
        """Agregar un item en la lista simple"""
        self._head = Nodo(item, self._head)

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



if __name__ == "__main__":
    l = ListaSimple()
    l.add(1)
    l.add(2)
    l.add(3)

    for i in l:
        print(i)

