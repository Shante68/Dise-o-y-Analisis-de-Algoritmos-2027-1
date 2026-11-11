
import sys

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
N = len(ALFABETO)

# Palabras muy frecuentes en español para identificar el texto correcto
PALABRAS_COMUNES = {
    "de", "la", "que", "el", "en", "y", "a", "los", "se", "del", "las",
    "un", "por", "con", "no", "una", "su", "para", "es", "al", "lo",
    "como", "mas", "pero", "sus", "le", "ya", "o", "este", "si", "porque",
}


def descifrar(texto, k):
    """Descifra el texto aplicando un desplazamiento k hacia atrás."""
    resultado = []
    for c in texto:
        minus = c.lower()
        if minus in ALFABETO:
            nueva = ALFABETO[(ALFABETO.index(minus) - k) % N]
            resultado.append(nueva.upper() if c.isupper() else nueva)
        else:
            resultado.append(c)  # espacios, puntuación, etc. se conservan
    return "".join(resultado)


def puntuar(texto):
    """Cuenta cuántas palabras del texto son palabras comunes del español."""
    palabras = "".join(c if c.isalpha() or c.isspace() else " " for c in texto.lower()).split()
    return sum(1 for p in palabras if p in PALABRAS_COMUNES)


def main():
    archivo = sys.argv[1] if len(sys.argv) > 1 else "mensajeCifrado.txt"
    with open(archivo, encoding="utf-8-sig") as f:  # utf-8-sig elimina el BOM
        cifrado = f.read()

    
    print("CIFRADO CÉSAR ")
    

    mejor_k, mejor_puntos = 0, -1
    for k in range(N):
        candidato = descifrar(cifrado, k)
        puntos = puntuar(candidato)
        primera_linea = candidato.splitlines()[0] if candidato else ""
        print(f"k = {k:2d} | puntos = {puntos:3d} | {primera_linea[:55]}")
        if puntos > mejor_puntos:
            mejor_k, mejor_puntos = k, puntos

    print("=" * 70)
    print(f"Desplazamiento encontrado: k = {mejor_k}")
    print("Mensaje descifrado:")
    print("-" * 70)
    print(descifrar(cifrado, mejor_k))
    print("-" * 70)


if __name__ == "__main__":
    main()
