from random import randint
import timeit
import time

def three_sum(a: list[int]) -> int:
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k]==0:
                    count +=1
    return count


def randomArray(n: int) -> list[int]:
    a = [ randint(-1000,1000) for i in range(n) ]
    return a



def medirTiempo1(n: int) -> float:
    '''Medir tiempo de ejecución usando timeit'''
    setup = '''
def three_sum(a: list[int]) -> int:
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k]==0:
                    count +=1
    return count

from random import randint
def randomArray(n: int) -> list[int]:
    a = [ randint(-1000,1000) for i in range(n) ]
    return a

a = randomArray(100)
    '''
    SAMPLES = 10
    t = timeit.timeit( setup=setup, stmt='three_sum(a)', number=SAMPLES )
    print("Tiempo promedio: ", t/SAMPLES)
    return t/SAMPLES


def medirTiempo2(n: int) -> float:
    a = randomArray(n)
    empieza = time.time()
    c = three_sum(a)
    termina = time.time()
    print(f"Conteo: {c}")
    print("Tiempo", termina-empieza )


if __name__ == "__main__":
    a = randomArray(100)
    c = three_sum(a)
    print(f"Conteo: {c}")

    medirTiempo1(100)

    medirTiempo2(100)