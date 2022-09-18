import sys
import time
from GenerarADTs import generar

# Métodos de ordenación que ofrece el Python
# https://docs.python.org/3/library/stdtypes.html#list.sort     # Método de list
# https://docs.python.org/3/howto/sorting.html                  # Función de biblioteca

# Métodos de ordenación del texto guía
# from algs4.selection import Selection
# from algs4.insertion import Insertion
# from algs4.shell import Shell
# from algs4.merge import Merge
# from algs4.quick import Quick


if __name__=="__main__":

    N=100

    inicio = time.time()
    listaPersonas = generar(N)
    termina = time.time()
    print(f"Tiempo para generar la lista: {termina-inicio:9.6f} segs")
    for n in listaPersonas:
        print(n)

    # Ejercicios
    # 1. Ordenar por apellido y nombre ascendiente
    # 2. Ordenar por edad ascendiente
    # 3. Ordenar por peso descendiente
    # 4. Ordenar por edad y peso

    # Medición de tiempos y comparación, para N grandes
    # 1. Generar un arreglo de tamaño N
    # 2. Hacer tres copias del arreglo
    # 3. Ordenar una copia por un método cuadratico
    # 4. Ordenar por un método linearitmético
    # 5. Ordenar por la biblioteca del lenguaje
    # 6. Comparar los tiempos obtenidos
    # 7. Hace diferencia en el tiempo si se ordenan ascendente/descendente ?
