def insercion_ordenar(arr):
    # Recorre el arreglo empezando por el segundo elemento
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        
        # Mueve los elementos mayores que la clave a una posición adelante
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Inserta la clave en su posición correcta
        arr[j + 1] = clave
    
    return arr

# Ejemplo de uso
arreglo = ['M','E','T','O','D','O','S','D','E','O','R','D','E','N','A','C','I','O','N']
arreglo_ordenado = insercion_ordenar(arreglo)
print("Arreglo ordenado:", arreglo_ordenado)
