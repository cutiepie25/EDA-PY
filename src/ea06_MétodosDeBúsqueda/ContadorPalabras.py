from typing import Dict
from sys import stdin


# TODO: Registrar el conteo de cada palabra en el diccionario
def wordCount(minLen: int) -> Dict[str, int]:
    conteo = dict()
    for line in stdin:
        if line=='':
            break
        words = line.split()
        print(words)

    return conteo


if __name__=="__main__":
    data = wordCount(3)
    # TODO: Mostrar la frecuencia de cada una de las palabras
