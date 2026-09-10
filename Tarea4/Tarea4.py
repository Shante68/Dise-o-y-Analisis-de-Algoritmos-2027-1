def busqueda_binaria(datos, buscado):
    lim_inf = 0
    lim_sup = len(datos) - 1
    pasos = 0

    while lim_inf <= lim_sup:
        pasos += 1
        mid = (lim_sup + lim_inf) // 2

        if datos[mid] == buscado:
            return mid, pasos
        
        if buscado < datos[mid]:
            lim_sup = mid - 1
        else:
            lim_inf = mid + 1

    return -1, pasos


tamanos = [10, 100, 1000, 10000, 100000, 1000000]

for n in tamanos:
    lista = list(range(n))
    buscado = n - 1
    
    posicion, pasos = busqueda_binaria(lista, buscado)
    print(f"Para n = {n}: encontrado en posición {posicion} en {pasos} pasos")