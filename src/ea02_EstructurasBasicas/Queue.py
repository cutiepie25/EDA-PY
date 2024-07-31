from dataclasses import dataclass

@dataclass
class Nodo:
    item: any
    next: 'Nodo'

class Queue:
    first: Nodo = None
    n: int = 0

    def enqueue(self,item:any) -> None:
        if self.first in None: 
            self.first = tmp
            self.last = tmp
        
        else:
            tmp = Nodo(item,None)
            self.last.next = tmp
            self.last = tmp
        self.n += 1

    def dequeue(self) -> any:
        if self.first is None:
            return None
        
        x = self.first.item
        self.first = self.first.next
        self.n -= 1
        return x

    def size(self) -> int:
        return self.n
    
    def isEmpty(self) -> bool:
        return self.first is None
    
    def __iter__(self):
        self.p = self.first
        return self
    
    def __next__(self):
        if self.p is None:
           raise StopIteration
        x = self.p.item
        self.p = self.p.next
        return x        


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue("uno")
    queue.enqueue("dos")
    queue.enqueue("tres")
    assert(not(queue.isEmpty()))
    assert(queue.size()==3)
    
    for x in queue:
        print(x)
        
        


   # print(queue.dequeue())
    #print(queue.dequeue())
    #print(queue.dequeue())
    #assert(queue.isEmpty())
    #assert(queue.size()==0)