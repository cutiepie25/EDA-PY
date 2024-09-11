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

def prueba_unitaria_diferente():
    # Muestras conocidas (vectores de dimensión 2) con sus respectivas clases
    conocidos = [
        [1.0, 1.0],   # Clase 0
        [1.5, 2.0],   # Clase 0
        [2.0, 1.0],   # Clase 1
        [3.0, 3.5],   # Clase 1
        [5.0, 5.0],   # Clase 2
        [6.0, 6.5],   # Clase 2
        [7.0, 8.0],   # Clase 2
        [0.5, 1.0]    # Clase 0
    ]
    
    clases = [0, 0, 1, 1, 2, 2, 2, 0]
    
    # Nuevas muestras desconocidas
    muestra_desconocida1 = [2.5, 2.0]  # Se espera que pertenezca a la clase 1
    muestra_desconocida2 = [6.0, 5.5]  # Se espera que pertenezca a la clase 2
    muestra_desconocida3 = [1.0, 1.5]  # Se espera que pertenezca a la clase 0
    
    k = 3  # Se considerarán los 3 vecinos más cercanos
    
    # Clasificar la primera muestra desconocida
    resultado1 = clasificar(conocidos, clases, muestra_desconocida1, k)
    print(f'La clase de la muestra desconocida1 es: {resultado1}')  # Debería ser 1
    
    # Clasificar la segunda muestra desconocida
    resultado2 = clasificar(conocidos, clases, muestra_desconocida2, k)
    print(f'La clase de la muestra desconocida2 es: {resultado2}')  # Debería ser 2
    
    # Clasificar la tercera muestra desconocida
    resultado3 = clasificar(conocidos, clases, muestra_desconocida3, k)
    print(f'La clase de la muestra desconocida3 es: {resultado3}')  # Debería ser 0

# Main para ejecutar la prueba
if __name__ == "__main__":
    prueba_unitaria_diferente()