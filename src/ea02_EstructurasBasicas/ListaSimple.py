

class Nodo:

    def __init__(self, item, next):
        self._item = item
        self._next = next


class ListaSimple:

    def __init__(self):
        self._head = None

    def add(self, item):
        self._head = Nodo(item, self._head)

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
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

