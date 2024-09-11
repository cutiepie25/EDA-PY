import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt

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
    * Al inicio del bucle se inicializa la variable distancias (operación unitaria) = 1
    * El bucle se ejecuta N veces, donde N es la cantidad de muestras = N
    * Cada iteración del bucle llama a calcular_distancia y cada iteración del bucle utiliza append que es una operación unitaria = 3M + 3
    * Total de operaciones del bucle = N(3M + 3)

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


# 4) Evaluar experimentalmente el desempeño del algoritmo en función del tamaño del dataset de puntos conocidos

# a) Generar un dataset de N puntos conocidos y su respectiva clase.
def generar_datos(N, d=2):
    X = np.random.rand(N, d) * 100  # Puntos aleatorios en el rango [0, 100]
    y = np.random.choice([0, 1], size=N)  # Clases aleatorias 0 o 1
    return X, y

# b) Tomar S=10 muestras desconocidas (generadas aleatoriamente), clasificarlas y tomar los tiempos.
def evaluar_rendimiento():
    tiempos = []
    # c) Tabular los datos para distintos valores de N empezando en 500 y doblando el tamaño.
    Ns = [500 * (2 ** i) for i in range(6)]  # [500, 1000, 2000, 4000, 8000, 16000]
    S = 10  # Número de muestras desconocidas a generar

    for N in Ns:
        # Generar dataset conocido de tamaño N
        conocidos, clases = generar_datos(N)

        # Generar S muestras desconocidas (en este caso de dimensión 2)
        muestras_desconocidas = np.random.rand(S, 2) * 100

        # Clasificar cada muestra desconocida y medir el tiempo
        tiempos_muestra = []
        for muestra in muestras_desconocidas:
            inicio = time.time()  # Iniciar medición de tiempo
            clasificar(conocidos, clases, muestra, k=5)  # Clasificar usando k-NN con k=5
            fin = time.time()  # Finalizar medición de tiempo
            tiempos_muestra.append(fin - inicio)  # Guardar el tiempo transcurrido

        # Calcular el tiempo promedio de clasificación para las S muestras
        tiempo_promedio = np.mean(tiempos_muestra)
        tiempos.append(tiempo_promedio)

    return Ns, tiempos

# d) Gráfica comparativa entre los tiempos promedios experimentales y estimaciones teóricas O(N log N).
def graficar_rendimiento(Ns, tiempos_experimentales, tiempos_analiticos):
    plt.plot(Ns, tiempos_experimentales, marker='o', label='Tiempos experimentales')
    plt.plot(Ns, tiempos_analiticos, marker='x', label='Estimación analítica O(N log N)')
    plt.title('Comparación de Tiempos: Experimental vs Analítico')
    plt.xlabel('Tamaño del dataset (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

# e) Estimar el tiempo de clasificación para un valor N no considerado en los experimentos.
def tiempo_analitico(Ns):
    return [N * np.log(N) for N in Ns]




"""# Main para ejecutar la prueba
if __name__ == "__main__":
    prueba_unitaria_diferente()
    print("")
    # Ejecutar la evaluación y graficar los resultados
    Ns, tiempos_experimentales = evaluar_rendimiento()  # Realizar los experimentos
    tiempos_analiticos = tiempo_analitico(Ns)  # Calcular los tiempos analíticos (O(N log N))
    graficar_rendimiento(Ns, tiempos_experimentales, tiempos_analiticos)  # Generar la gráfica"""

if __name__ == "__main__":
    # Pruebas unitarias
    prueba_unitaria_diferente()
    print("\nTodas las pruebas unitarias pasaron correctamente.\n")

    # Numeral 4a: Generar un dataset de N puntos conocidos y su respectiva clase.
    print("Numeral 4a: Generar un dataset de N puntos conocidos y su respectiva clase.")

    # Numeral 4b: Tomar S=10 muestras desconocidas, clasificarlas y medir los tiempos.
    print("\nNumeral 4b: Clasificación de S=10 muestras desconocidas para diferentes tamaños de N.")
    Ns, tiempos_experimentales = evaluar_rendimiento()
    for N, tiempo in zip(Ns, tiempos_experimentales):
        print(f"Tamaño del dataset (N): {N}, Tiempo promedio de clasificación: {tiempo:.6f} segundos")

    # Numeral 4c: Tabular los datos para distintos valores de N.
    print("\nNumeral 4c: Tabulación de los tiempos promedio para distintos valores de N.")
    print(f"{'Tamaño del dataset (N)':<25} {'Tiempo promedio (segundos)':<30}")
    for N, tiempo in zip(Ns, tiempos_experimentales):
        print(f"{N:<25} {tiempo:<30}")

    # Numeral 4d: Graficar los tiempos promedios y compararlos con la estimación analítica O(N log N)
    tiempos_analiticos = tiempo_analitico(Ns)
    print("\nNumeral 4d: Comparación gráfica entre tiempos experimentales y teóricos O(N log N).")
    graficar_rendimiento(Ns, tiempos_experimentales, tiempos_analiticos)

    # Numeral 4e: Estimar el tiempo de clasificación para un valor N no considerado en los experimentos.
    print("\nNumeral 4e: Estimar el tiempo de clasificación para un valor N no considerado en los experimentos.")
    N_nuevo = 7000
    conocidos_nuevos, clases_nuevas = generar_datos(N_nuevo)
    muestras_nuevas = np.random.rand(10, 2) * 100

    tiempos_nuevos = []
    for muestra in muestras_nuevas:
        inicio = time.time()
        clasificar(conocidos_nuevos, clases_nuevas, muestra, k=5)
        fin = time.time()
        tiempos_nuevos.append(fin - inicio)

    tiempo_promedio_nuevo = np.mean(tiempos_nuevos)
    tiempo_analitico_nuevo = N_nuevo * np.log(N_nuevo)

    print(f"Tamaño del dataset (N): {N_nuevo}")
    print(f"Tiempo promedio de clasificación (experimental): {tiempo_promedio_nuevo:.6f} segundos")
    print(f"Tiempo estimado (teórico O(N log N)): {tiempo_analitico_nuevo:.6f} segundos")
