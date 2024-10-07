def seleccion_ordenar(arr):
    # Recorre todo el arreglo
    for i in range(len(arr)):
        # Encuentra el mínimo elemento en el resto del arreglo no ordenado
        indice_minimo = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        # Intercambia el elemento mínimo con el primer elemento no ordenado
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return arr

# Ejemplo de uso
arreglo = ['M','E','T','O','D','O','S','D','E','O','R','D','E','N','A','C','I','O','N']
arreglo_ordenado = seleccion_ordenar(arreglo)
print("Arreglo ordenado:", arreglo_ordenado)
