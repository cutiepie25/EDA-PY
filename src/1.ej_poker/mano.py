from naipe import Naipe
from carta import Carta
from collections import Counter

class Mano:
    def __init__(self, naipe: Naipe):
        self.cartas = [naipe.tomar_carta() for _ in range(5)]

    def reemplazar(self, carta_a_eliminar: Carta, naipe: Naipe):
        # Eliminar la carta específica de la mano
        self.cartas.remove(carta_a_eliminar)
        # Tomar una nueva carta del Naipe
        self.cartas.append(naipe.tomar_carta())

    def comparar(self, otra_mano) -> bool:
        # Implementar comparación de manos según reglas del póker
        return self.obtener_valor_mano() > otra_mano.obtener_valor_mano()
    
    def obtener_valor_mano(self) -> tuple:
        valores = sorted([carta.get_valor() for carta in self.cartas], reverse=True)
        unique_values = set(valores)
        pinta_set = set([carta.pinta for carta in self.cartas])
        
        # Comprobar si es una escalera
        if len(unique_values) == 5 and max(unique_values) - min(unique_values) == 4:
            if len(pinta_set) == 1:
                return (9, max(valores))  # Straight Flush
            return (5, max(valores))  # Straight

        # Comprobar si es un flush
        if len(pinta_set) == 1:
            return (6, valores)  # Flush

        # Contar las ocurrencias de cada valor
        valor_count = Counter(valores)

        if 4 in valor_count.values():
            return (8, valores)  # Four of a Kind
        elif 3 in valor_count.values() and 2 in valor_count.values():
            return (7, valores)  # Full House
        elif 3 in valor_count.values():
            return (4, valores)  # Three of a Kind
        elif list(valor_count.values()).count(2) == 2:
            return (3, valores)  # Two Pair
        elif 2 in valor_count.values():
            return (2, valores)  # One Pair
        else:
            return (1, valores)  # High Card
    
    def comparar(self, otra_mano) -> bool:
        return self.obtener_valor_mano() > otra_mano.obtener_valor_mano()
    
    def __str__(self):
        return ', '.join(str(carta) for carta in self.cartas)