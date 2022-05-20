from random import randint
import time


N = 1000
datos = [ randint(0,N) for i in range(N) ]
print('Datos no ordenados', datos[:10])

copia1 = datos.copy()
copia1.sort()
print('Orden ascendente', copia1[:10])

copia2 = datos.copy()
copia2.sort(reverse=True)
print('Orden descendente', copia2[:10])

copia3 = sorted(datos)
copia4 = sorted(datos, reverse=True)
print('copia3', copia3[:10])
print('copia4', copia4[:10])
print('datos', datos[:10])

# Prueba de doblaje
while(N<50000):
    datos = [ randint(0,N) for i in range(N) ]
    inicio = time.time()
    datos.sort()
    termina = time.time()
    print('N = {0:6d} , Tiempo = {1:9.6f}'.format(N, termina-inicio))
    N *= 2


# Ejercicios
# 1. Ordenar una lista de Puntos2D por su magnitud
# 2. Ordenar una lista objetos Fecha
# 3. Crear una lista de nombres (GeneradorNombres) y ordenarlos alfabeticamente
# 4. Cual es la diferencia entre .sort y sorted() ?