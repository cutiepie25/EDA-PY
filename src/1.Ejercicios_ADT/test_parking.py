from parking import Parqueadero
import unittest

class TestConcreteParkingLotCounter(unittest.TestCase):
    def setUp(self):
        self.Parqueadero = Parqueadero.contador_parqueadero(10)  # Iniciar con 10 espacios disponibles

    def test_entrada(self):
        self.Parqueadero()
        self.assertEqual(self.parking_lot.obtener_espacios_disponibles(), 9)

    def test_salida(self):
        self.parking_lot.entrada()  # Decrementa a 9
        self.parking_lot.salida()   # Incrementa a 10
        self.assertEqual(self.parking_lot.obtener_espacios_disponibles(), 10)

    def test_no_entrada_cuando_lleno(self):
        parking_lot_full = ConcreteParkingLotCounter(1)  # Solo un espacio disponible
        parking_lot_full.entrada()  # Se llena el espacio
        parking_lot_full.entrada()  # No debería cambiar el contador
        self.assertEqual(parking_lot_full.obtener_espacios_disponibles(), 0)

    def test_no_salida_cuando_vacio(self):
        parking_lot_full = ConcreteParkingLotCounter(1)  # Solo un espacio disponible
        parking_lot_full.salida()  # Intentar incrementar más allá del límite inicial
        parking_lot_full.salida()  # No debería cambiar el contador
        self.assertEqual(parking_lot_full.obtener_espacios_disponibles(), 1)

if __name__ == '__main__':
    unittest.main()
