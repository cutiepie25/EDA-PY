# Cola de minima prioridad de la libreria estandar de Python: heapq
# REF:
# https://docs.python.org/3/library/heapq.html


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


