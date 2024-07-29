from dataclasses import dataclass

@dataclass
class Nodo:
    item: any
    next: 'Nodo'

class Queue:
    first: Nodo = None
    n: int = 0

    def enqueue(self,item:any) -> None:
        # TODO : Implementar metodo enqueue
        pass

    def dequeue(self) -> any:
        # TODO : Implementar metodo dequeue
        pass

    def size(self) -> int:
        return self.n
    
    def isEmpty(self) -> bool:
        return self.first is None


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue("uno")
    queue.enqueue("dos")
    queue.enqueue("tres")
    assert(not(queue.isEmpty()))
    assert(queue.size()==3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    assert(queue.isEmpty())
    assert(queue.size()==0)