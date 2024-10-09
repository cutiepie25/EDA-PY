def natural_merge_sort(arr):
    # Función para fusionar dos listas ordenadas
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Agregar el resto de los elementos si quedan en alguna de las listas
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Identificar "runs" naturales (subsecuencias ya ordenadas)
    def find_runs(arr):
        runs = []
        new_run = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:  # Si sigue en orden ascendente
                new_run.append(arr[i])
            else:
                runs.append(new_run)  # Cierra la run y comienza una nueva
                new_run = [arr[i]]

        runs.append(new_run)  # Añade la última run
        return runs

    # Algoritmo principal
    while True:
        runs = find_runs(arr)
        if len(runs) == 1:
            # Si solo queda una run, ya está ordenado
            return runs[0]
        
        # Fusionar las runs de dos en dos
        new_arr = []
        for i in range(0, len(runs) - 1, 2):
            merged = merge(runs[i], runs[i + 1])
            new_arr.append(merged)

        if len(runs) % 2 == 1:  # Si hay un run restante sin fusionar
            new_arr.append(runs[-1])

        arr = [item for sublist in new_arr for item in sublist]  # Aplanar lista

# Ejemplo de uso
arreglo = ['M','E','T','O','D','O','S','D','E','O','R','D','E','N','A','C','I','O','N']
arreglo_ordenado = natural_merge_sort(arreglo)
print("Arreglo ordenado:", arreglo_ordenado)
