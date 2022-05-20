from algs4.selection import Selection
from algs4.insertion import Insertion
from algs4.shell import Shell
from algs4.merge import Merge
from algs4.quick import Quick
from random import randint
import time


if __name__ == '__main__':
    N = 10000
    datos = [ randint(0,N) for i in range(N) ]

    copia = datos.copy()
    inicia = time.time()
    Selection.sort(copia)
    finaliza = time.time()
    print(copia[:20], finaliza-inicia)

    copia = datos.copy()
    inicia = time.time()
    Insertion.sort(copia)
    finaliza = time.time()
    print(copia[:20], finaliza-inicia)

    copia = datos.copy()
    inicia = time.time()
    Shell.sort(copia)
    finaliza = time.time()
    print(copia[:20], finaliza-inicia)

    copia = datos.copy()
    inicia = time.time()
    Merge.sort(copia)
    finaliza = time.time()
    print(copia[:20], finaliza-inicia)

    copia = datos.copy()
    inicia = time.time()
    Quick.sort(copia)
    finaliza = time.time()
    print(copia[:20], finaliza-inicia)

# Ejercicios
# 1. Hacer pruebas para distintos valores de N y graficar la curva para cada algoritmo
# 2. Comparar eficiencia con el metodo .sort de las listas en Python

