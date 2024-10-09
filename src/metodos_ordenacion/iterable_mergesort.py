def merge_sort_iterativo(arr):
    # Función para fusionar dos mitades
    def fusionar(arr, izq, medio, der):
        # Dividir las dos mitades
        izquierda = arr[izq:medio+1]
        derecha = arr[medio+1:der+1]
        
        i = j = 0
        k = izq
        
        # Fusionar ambas listas ordenadas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1
        
        # Si quedan elementos en la izquierda
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1
        
        # Si quedan elementos en la derecha
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1
    
    # Enfoque de mezcla de tamaño creciente
    n = len(arr)
    sub_tamano = 1
    
    while sub_tamano < n:
        for izq in range(0, n, 2*sub_tamano):
            medio = min(n - 1, izq + sub_tamano - 1)
            der = min(n - 1, izq + 2*sub_tamano - 1)
            fusionar(arr, izq, medio, der)
        sub_tamano *= 2
    
    return arr

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
arr_ordenado = merge_sort_iterativo(arr)
print("Arreglo ordenado (Merge Sort Iterativo):", arr_ordenado)
