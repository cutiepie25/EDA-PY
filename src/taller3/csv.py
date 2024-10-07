import pandas as pd

class Pelicula:
    def _init_(self, titulo, domestic_gross, profit, roi, vote_average):
        self.titulo = titulo
        self.domestic_gross = domestic_gross
        self.profit = profit
        self.roi = roi
        self.vote_average = vote_average

    def _str_(self):
        return f"{self.titulo} - Domestic Gross: {self.domestic_gross}, Profit: {self.profit}, ROI: {self.roi}, Vote Average: {self.vote_average}"

def leer_peliculas_desde_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)
    
    peliculas = []
    for _, fila in df.iterrows():
        titulo = fila['title']
        domestic_gross = fila['domestic_gross']
        profit = fila['profit']
        roi = fila['roi']
        vote_average = fila['vote_average']
        
        pelicula = Pelicula(titulo, domestic_gross, profit, roi, vote_average)
        peliculas.append(pelicula)
    
    return peliculas

# Ejemplo de uso:
ruta_csv = 'C:/Users/Aleja/MiCarpeta/EDA-PY/src/taller3'
peliculas = leer_peliculas_desde_csv(ruta_csv)

for pelicula in peliculas[:5]:
   print(pelicula)