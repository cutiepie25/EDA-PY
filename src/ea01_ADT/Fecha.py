

class Fecha:

    def __init__(self, año:int, mes:int, dia:int):
        self._año = año
        self._mes = mes
        self._dia = dia

    def diaDelAño(self) -> int:
        # TODO Implementar el calculo del dia del año
        pass

    def esBiciesto(año: int) -> bool:
        # TODO Implementar la funcion para determinar si un año es biciesto
        pass

    def __str__(self) -> str:
        # TODO Implementar la conversion a formato string
        pass

    def leerFecha():
        # TODO Leer una fecha por consola y returnar una instancia de Fecha
        pass


if __name__ == "__main__":
    fecha = Fecha(2022,5,17)
    # TODO hacer pruebas unitarias de Fecha
    