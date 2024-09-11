import random
from carta import Carta

class Naipe:
    def __init__(self):
        valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        pintas = ["♠", "♥", "♦", "♣"]
        self.cartas=[Carta(valor,pinta) for valor in valores for pinta in pintas]
        random.shuffle(self.cartas)
        
    def tomarCarta(self) -> 'Carta':
        if len(self.cartas) == 0:
            return None
        return self.cartas.pop()
    
