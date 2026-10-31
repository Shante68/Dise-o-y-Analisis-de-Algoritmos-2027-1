def dos_suma(nums, objetivo):

    tabla_hash = {}

    for indice, num in enumerate(nums):
        complemento = objetivo - num

        if complemento in tabla_hash:
            return [tabla_hash[complemento], indice]

        tabla_hash[num] = indice

    return None


arreglo = [2, 14, 6, 11, 8, 15, 7]
objetivo = 9

print(f"Arreglo: {arreglo}")
print(f"Objetivo: {objetivo}")
print("-" * 50)

resultado = dos_suma(arreglo, objetivo)

if resultado:
    i, j = resultado
    print(f"Índices encontrados: [{i}, {j}]")
    print(f"Valores correspondientes: {arreglo[i]} + {arreglo[j]} = {objetivo}")
else:
    print("No se encontró ninguna pareja que sume el objetivo.")
