def calcular_distancia(punto1, punto2):
    """Calcula la distancia euclidiana entre dos puntos de dimensión d."""
    suma = 0.0
    for i in range(len(punto1)):
        suma += (punto1[i] - punto2[i]) ** 2
    return suma ** 0.5  # Raíz cuadrada manual

def clasificar(conocidos, clases, desconocido, k):
    """
    clasificar - Clasifica una muestra desconocida utilizando el algoritmo kNN.

    conocidos: Matriz de N muestras (vectores de dimensión d).
    clases: Lista de clases correspondientes a las muestras conocidas.
    desconocido: Muestra de dimensión d a clasificar.
    k: Número de vecinos más cercanos a considerar.
    """
    # Paso 1: Calcula la distancia entre la muestra desconocida y todas las conocidas
    distancias = []
    for i in range(len(conocidos)):
        distancia = calcular_distancia(conocidos[i], desconocido)
        distancias.append((distancia, clases[i]))

    # Paso 2: Ordenar las distancias utilizando la función sort
    distancias.sort(key=lambda x: x[0])

    # Paso 3: Seleccionar las clases de los k vecinos más cercanos
    vecinos_clases = [distancias[i][1] for i in range(k)]

    # Paso 4: Devolver la clase más común entre los k vecinos
    conteo = {}
    for clase in vecinos_clases:
        if clase in conteo:
            conteo[clase] += 1
        else:
            conteo[clase] = 1

    clase_mas_comun = max(conteo, key=conteo.get)
    return clase_mas_comun