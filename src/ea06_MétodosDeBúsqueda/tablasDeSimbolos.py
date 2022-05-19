from random import randint
import time
from algs4.sequential_search_st import SequentialSearchST
from algs4.binary_search_st import BinarySearchST
from algs4.bst import BST
from algs4.red_black_bst import RedBlackBST


def nombreClase(clase):
    pos = str(clase.__class__).find('st.')
    return str(clase.__class__)[pos+3:-2]


def medirInsercionDatos(st, datos):
    inicia = time.time()
    for (llave,valor) in datos:
        st.put(llave,valor)
    termina = time.time()
    print('{:>18s}.insert: N={}, tiempo={:9.6f}'.format(nombreClase(st), len(datos), termina-inicia))

def medirBusquedaDatos(st, buscar):
    inicia = time.time()
    for llave in buscar:
        st.get(llave)
    termina = time.time()
    print('{:>18s}.get   : N={}, tiempo={:9.6f}'.format(nombreClase(st), len(datos), termina-inicia))


# TODO Hacer una funcion para medir los tiempos de borrado de datos
def medirBorrado(st, borrar):
    pass


if __name__ == '__main__':

    N = 10000
    datos = [ (randint(0,N),f'Valor={i}') for i in range(N) ]
    buscar = [ datos[randint(0,len(datos)-1)][0] for i in range(N) ]
    print(datos[:10])
    print(buscar[:10])
    print()

    secuencial = SequentialSearchST()
    medirInsercionDatos(secuencial, datos)
    medirBusquedaDatos(secuencial, buscar)
    print()

    binaria = BinarySearchST()
    medirInsercionDatos(binaria, datos)
    medirBusquedaDatos(binaria, buscar)
    print()

    arbolBinario = BST()
    medirInsercionDatos(arbolBinario, datos)
    medirBusquedaDatos(arbolBinario, buscar)
    print()

    arbolRojoNegro = RedBlackBST()
    medirInsercionDatos(arbolRojoNegro, datos)
    medirBusquedaDatos(arbolRojoNegro, buscar)
    print()

