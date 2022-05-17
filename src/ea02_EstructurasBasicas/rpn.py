from algs4.stack import Stack


# Nota:
# En Linux terminar con ctrl-d
# En windows terminar con ctrl-z
def calcular() -> float:
    pila = Stack()
    while(True):
        try: 
            linea = input()
            if linea.isnumeric():           # TODO: isnumeric no acepta valores con decimales
                pila.push(float(linea))

        except EOFError:
            break
        # TODO - Acabar la implementacion de la calculadora RPN
    return pila.pop()


if __name__=="__main__":
    resultado = calcular()
    print(resultado)

