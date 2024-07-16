

class Fecha:

    def __init__(self, año:int, mes:int, dia:int):
        self._año = año
        self._mes = mes
        self._dia = dia

    def diaDelAño(self) -> int:
        # TODO Implementar el calculo del dia del año
        pass

    @staticmethod
    def esBiciesto(año: int) -> bool:
        # TODO Implementar la funcion para determinar si un año es biciesto
        pass

    def __str__(self) -> str:
        return f"{self._año:4d}-{self._mes:02d}-{self._dia:02d}"

    def __lt__(self, fecha) -> bool:
        # TODO Implementar la comparacion 'menor que' entre fechas
        pass

    def __eq__(self, fecha) -> bool:
        # TODO Implementar la igualdad entre instancias de Fecha
        pass

    @staticmethod
    def leerFecha() -> 'Fecha':
        """[Factory Pattern](https://refactoring.guru/design-patterns/factory-method)"""
        # TODO Leer una fecha por consola y returnar una instancia de Fecha
        pass


if __name__ == "__main__":

    cumple = Fecha.leerFecha()      # Invocar un método estático

    fecha = Fecha(2022,5,9)         # Invocar el constructor
    print(fecha)

    # TODO hacer pruebas unitarias de Fecha
    