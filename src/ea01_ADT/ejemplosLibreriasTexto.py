import stdio
import stdrandom
# import stdstats       # Nota: No se puede utilizar sin pygame


def entradas_y_salidas():
    pop = 5
    stdio.writeln(f"Hello World, we are now {pop}")
    stdio.write("Ingrese un int: ")
    a = stdio.readInt()
    stdio.write("Ingrese un float: ")
    b = stdio.readFloat()

def ejemplos_stdrandom():
    lista1 = [ stdrandom.uniformInt(5,10) for i in range(10) ]
    stdio.writeln(lista1)
    stdrandom.shuffle(lista1)
    stdio.writeln(lista1)
    lista2 = [ stdrandom.uniformFloat(5,10) for i in range(10) ]
    stdio.writeln(lista2)
    lista3 = [ stdrandom.gaussian(mean=5, stddev=2) for i in range(10) ]
    stdio.writeln(lista3)

# def ejemplos_stdstats():
#     lista3 = [ stdrandom.gaussian(mean=5, stddev=2) for i in range(100) ]
#     promedio = stdstats.mean(lista3)
#     varianza = stdstats.var(lista3)
#     stddev = stdstats.stddev(lista3)
#     mediana = stdstats.median(lista3)
#     stdio.writeln(f"Promedio = {promedio}, varianza = {varianza}, desv.std = {stddev}, mediana = {mediana}")


if __name__=="__main__":
    entradas_y_salidas()
    ejemplos_stdrandom()
    # ejemplos_stdstats()