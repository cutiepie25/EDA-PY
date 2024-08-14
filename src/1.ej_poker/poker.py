import random

class Carta:
    def __init__(self, valor: str, pinta: str):
        self.valor = valor
        self.pinta = pinta
    
    def get_valor(self) -> str:
        return self.valor
    
    def get_pinta(self) -> str:
        return self.pinta
    
    def to_string(self) -> str:
        return f"{self.valor} de {self.pinta}"
    

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
    
class Mano:
    def __init__(self):
        