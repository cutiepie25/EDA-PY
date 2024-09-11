def calcular_distancia(punto1, punto2):
    suma = 0.0
    for i in range(len(punto1)):# Sea N = longitud del vector punto1
        suma += (punto1[i] - punto2[i]) ** 2 #Operación unitaria
    return suma ** 0.5
"""
* Al inicio del bucle se inicializa la variable suma (operación unitaria) = 1
* El bucle se ejecuta M veces = M
* Por cada iteración (de las n iteraciones), se realizan 3 operaciones (resta, potencia y suma) 3
* El total de operaciones dentro del bucle son 3M
* Al final del bucle, se realiza una operación de raíz cuadrada, que es una operación unitaria = 1

T(calcular_distancia) = 3M+2
"""


def clasificar(conocidos: list, clases: list, desconocido:list, k:int):
    # Paso 1: Calcula la distancia entre la muestra desconocida y todas las conocidas
    distancias = []
    for i in range(len(conocidos)): #N veces
        distancia = calcular_distancia(conocidos[i], desconocido)
        distancias.append((distancia, clases[i]))
    """ 
    • Al inicio del bucle se inicializa la variable distancias (operación unitaria) = 1
    • El bucle se ejecuta N veces, donde N es la cantidad de muestras = N
    • Cada iteración del bucle llama a calcular_distancia y cada iteración del bucle utiliza append que es una operación unitaria = 3M + 3
    • Total de operaciones del bucle = N(3M + 3)

    T(distancia) = N(3M + 3) + 1
    """

    # Paso 2: Ordenar las distancias utilizando la función sort
    distancias.sort(key=lambda x: x[0])
    """ T(ordenar) = n log n """


    # Paso 3: Seleccionar las clases de los k vecinos más cercanos
    vecinos_clases = [distancias[i][1] for i in range(k)]
    """
    Cantidad de K vecinos más cercanos que seleccionamos después de calcular y ordenar las distancias.

    T(selección) = K """

    # Paso 4: Devolver la clase más común entre los k vecinos
    conteo = {}
    for clase in vecinos_clases:
        if clase in conteo:
            conteo[clase] += 1
        else:
            conteo[clase] = 1

    clase_mas_comun = max(conteo, key=conteo.get)
    return clase_mas_comun
    """
    * Contamos cuántas veces aparece cada clase en los k vecinos más cercanos = k
    * Para cada uno de los k vecinos, comprobamos si su clase ya está en el diccionario conteo. Si está, incrementamos su contador; si no, agregamos una nueva entrada al diccionario. = k
    * Cada inserción o actualización en el diccionario toma una operación unitaria, y esto se repite k veces. = k
    
    T(conteo) = 3k"""

"""
3) Estimar el tiempo requerido por el algoritmo clasificar

T(Total) = T(distancia) + T(ordenar)+ T(selección) + T(conteo)
T(Total) = N(3M + 3) + 1 + n log n + K + 3k
T(Total) = 3NM+3N+NlogN+1+4K
Notación tilde = 3NM + NLogN
Notación Big O = O(NM+NlogN)

"""
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
    assert resultado1 == 1, f'Error: se esperaba clase 1 para muestra desconocida1, obtenido: {resultado1}'
    
    # Clasificar la segunda muestra desconocida
    resultado2 = clasificar(conocidos, clases, muestra_desconocida2, k)
    assert resultado2 == 2, f'Error: se esperaba clase 2 para muestra desconocida2, obtenido: {resultado2}'
    
    # Clasificar la tercera muestra desconocida
    resultado3 = clasificar(conocidos, clases, muestra_desconocida3, k)
    assert resultado3 == 0, f'Error: se esperaba clase 0 para muestra desconocida3, obtenido: {resultado3}'
    
    print("Todas las pruebas unitarias pasaron correctamente.")

# Main para ejecutar la prueba
if __name__ == "__main__":
    prueba_unitaria_diferente()
