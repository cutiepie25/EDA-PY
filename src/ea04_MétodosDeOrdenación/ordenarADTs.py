import sys
from GenerarADTs import generar


if __name__=="__main__":

    listaPersonas = generar(100)
    # for n in listaPersonas:
    #     print(n)

    # list.sort method 

    # Ordernar utilizando el comparador del ADT: __lt__
    # listaPersonas.sort()
    # for n in listaPersonas:
    #     print(n)


    # Ordenar utilizando una función para extraer la llave de comparación
    # compKey = lambda p: str(p)
    # compKey = lambda p: p.apellidos+" "+p.nombres
    # compKey = lambda p: p.edad
    # listaPersonas.sort(key=compKey)
    # for n in listaPersonas:
    #     print(n)


    # sorted

    compKey = lambda p: p.edad
    listaOrdenada = sorted(listaPersonas, key=compKey)
    for n in listaOrdenada:
        print(n)
