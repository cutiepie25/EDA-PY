# Cola de minima prioridad de la libreria estandar de Python: heapq

import heapq
from random import randint

N = 100
datos = [ randint(0,N) for i in range(N) ]

monticulo = []
for x in datos:
    heapq.heappush(monticulo,x)

print('Monticulo\n', monticulo, sep='')

while len(monticulo)>0:
    x = heapq.heappop(monticulo)
    print(x, end=' ')
print()


datos2 = [ randint(0,N) for i in range(N) ]
heapq.heapify(datos2)
print('Monticulo de datos2:', datos2)

datos3 = [ randint(0,N) for i in range(N) ]
print('Top10', heapq.nlargest(10, datos3))
print('10 menores', heapq.nsmallest(10, datos3))