def mergeSort(data):
    tam = len(data)
    if tam <= 1:
        return data

    mid = tam // 2
    print("Izquierda", data[:mid:], end='| | ')
    print("Derecha", data[mid::])
    I = mergeSort(data[:mid:])
    D = mergeSort(data[mid::])

    return merge(I, D)


def merge(I, D):
    resultado = [None] * (len(I) + len(D))
    i = 0
    j = 0
    k = 0
    while i < len(I) and j < len(D):
        if I[i] <= D[j]:
            resultado[k] = I[i]
            i += 1
        else:
            resultado[k] = D[j]
            j += 1
        k += 1

    while i < len(I):
        resultado[k] = I[i]
        i += 1
        k += 1

    while j < len(D):
        resultado[k] = D[j]
        j += 1
        k += 1
    return resultado



datos_tarea = [45, 12, 78, 34, 61, 23, 50, 19, 72, 28, 55]

print("Lista original (11 elementos):", datos_tarea)
print("-" * 50)
print("Ejecución recursiva de mergeSort:")
print("-" * 50)

resultado_ordenado = mergeSort(datos_tarea)

print("-" * 50)
print("Lista final ordenada:", resultado_ordenado)
