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