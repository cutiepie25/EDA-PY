import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from PIL import Image
from IPython.display import Image as IPImage

class Pelicula:
    def __init__(self, movie, year, domestic_gross, profit, roi, vote_average):
        self.movie = movie.strip()
        self.year = year
        self.domestic_gross = domestic_gross
        self.profit = profit
        self.roi = roi
        self.vote_average = vote_average

    def __str__(self):
        return f"{self.movie} ({self.year}) - Gross: {self.domestic_gross}, Profit: {self.profit}, ROI: {self.roi}, Vote Average: {self.vote_average}"

    def __lt__(self, otra):
        return self.year < otra.year

    def __le__(self, otra):
        return self.year <= otra.year

    def __eq__(self, otra):
        return self.year == otra.year

    def __ne__(self, otra):
        return self.year != otra.year

    def __gt__(self, otra):
        return self.year > otra.year

    def __ge__(self, otra):
        return self.year >= otra.year


class Taller3:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.peliculas = self.cargar_peliculas_desde_csv()

    def cargar_peliculas_desde_csv(self):
        peliculas = []
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as file:
                encabezado = file.readline().strip().split(',')

                for linea in file:
                    valores = self.split_csv_line(linea.strip())

                    try:
                        movie = valores[encabezado.index('movie')]
                        year = int(valores[encabezado.index('year')])
                        domestic_gross = float(valores[encabezado.index('domestic_gross')]) if valores[encabezado.index('domestic_gross')] else 0.0
                        profit = float(valores[encabezado.index('profit')]) if valores[encabezado.index('profit')] else 0.0
                        roi = float(valores[encabezado.index('roi')]) if valores[encabezado.index('roi')] else 0.0
                        vote_average = float(valores[encabezado.index('vote_average')]) if valores[encabezado.index('vote_average')] else 0.0
                    except (ValueError, IndexError) as e:
                        print(f"Error al procesar la línea: {linea} - {e}")
                        continue

                    pelicula = Pelicula(movie, year, domestic_gross, profit, roi, vote_average)
                    peliculas.append(pelicula)

            print(f"Se cargaron {len(peliculas)} películas correctamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo_csv} no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al cargar las películas: {e}")

        return peliculas

    @staticmethod
    def split_csv_line(linea):
        elementos = []
        temp = ""
        dentro_comillas = False

        for char in linea:
            if char == '"' and not dentro_comillas:
                dentro_comillas = True
            elif char == '"' and dentro_comillas:
                dentro_comillas = False
            elif char == ',' and not dentro_comillas:
                elementos.append(temp.strip())
                temp = ""
            else:
                temp += char

        if temp:
            elementos.append(temp.strip())

        return elementos

    def encontrar_top_m_peliculas(self, peliculas, criterio, m):
        if criterio == 'domestic_gross':
            peliculas_ordenadas_por_criterio = sorted(peliculas, key=lambda p: p.domestic_gross, reverse=True)
        elif criterio == 'profit':
            peliculas_ordenadas_por_criterio = sorted(peliculas, key=lambda p: p.profit, reverse=True)
        elif criterio == 'roi':
            peliculas_ordenadas_por_criterio = sorted(peliculas, key=lambda p: p.roi, reverse=True)
        elif criterio == 'vote_average':
            peliculas_ordenadas_por_criterio = sorted(peliculas, key=lambda p: p.vote_average, reverse=True)
        else:
            raise ValueError("Criterio de ordenación no válido")

        top_m_peliculas = peliculas_ordenadas_por_criterio[:m]
        top_m_peliculas_ordenadas_por_ano = sorted(top_m_peliculas, reverse=True)

        return top_m_peliculas_ordenadas_por_ano

    def generar_grafico_barras(self, top_m_peliculas, criterio, ano, nombre_imagen):
        nombres = [p.movie for p in top_m_peliculas]
        valores = []

        if criterio == 'domestic_gross':
            valores = [p.domestic_gross for p in top_m_peliculas]
        elif criterio == 'profit':
            valores = [p.profit for p in top_m_peliculas]
        elif criterio == 'roi':
            valores = [p.roi for p in top_m_peliculas]
        elif criterio == 'vote_average':
            valores = [p.vote_average for p in top_m_peliculas]

        # Verificar si hay películas en la lista
        if not top_m_peliculas:
            print(f"No se encontraron películas para el año {ano} con el criterio {criterio}.")
            return

        # Verificar el contenido de las películas y los valores
        print(f"Películas encontradas para el año {ano}: {nombres}")
        print(f"Valores correspondientes: {valores}")

        # Generar gráfico
        plt.clf()  # Limpia el gráfico actual antes de generar uno nuevo
        plt.figure(figsize=(10, 6))
        plt.barh(nombres, valores, color='skyblue')
        plt.xlabel(criterio.capitalize())
        plt.title(f"Top-{len(top_m_peliculas)} Películas hasta el año {ano}")
        plt.gca().invert_yaxis()  # Invertir para que el top esté arriba
        plt.savefig(nombre_imagen)
        plt.show()
        plt.close()

    def solicitar_criterio_m_y_ano(self):
        # Preguntar al usuario el criterio de ordenación
        criterio = input("Ingrese el criterio para ordenar (domestic_gross, profit, roi, vote_average): ").strip()

        # Validar que el criterio sea válido
        if criterio not in ['domestic_gross', 'profit', 'roi', 'vote_average']:
            print("Criterio no válido. Intente de nuevo.")
            return

        # Preguntar al usuario el número de películas para el Top-M
        try:
            m = int(input("Ingrese el número de películas para el Top-M: "))
        except ValueError:
            print("Debe ingresar un número válido para M.")
            return

        # Preguntar al usuario el año límite
        try:
            ano_limite = int(input("Ingrese el año límite hasta el cual desea generar los gráficos: "))
        except ValueError:
            print("Debe ingresar un año válido.")
            return

        # Generar gráficos evolutivos desde el año límite hasta el año más antiguo
        self.generar_graficos_evolutivos(criterio, m, ano_limite, carpeta_imagenes)
        self.generar_animacion_evolutiva(carpeta_imagenes)

    def generar_graficos_evolutivos(self, criterio, m, ano_limite, carpeta_imagenes):
            # Obtener el año mínimo en el dataset
            min_year = min(self.peliculas, key=lambda p: p.year).year

            # Crear la carpeta si no existe
            if not os.path.exists(carpeta_imagenes):
                os.makedirs(carpeta_imagenes)

            # Generar gráficos acumulados empezando por el año límite y retrocediendo hasta el año más antiguo
            for ano in range(ano_limite, min_year - 1, -1):
                peliculas_hasta_ano = [p for p in self.peliculas if p.year <= ano]

                if not peliculas_hasta_ano:
                    print(f"No se encontraron películas hasta el año {ano}.")
                    continue

                # Encontrar las Top-M películas hasta el año actual de la iteración
                top_m_peliculas = self.encontrar_top_m_peliculas(peliculas_hasta_ano, criterio, m)

                # Mostrar las películas en consola
                print(f"\nTop-{m} películas hasta el año {ano}:")
                for pelicula in top_m_peliculas:
                    print(pelicula)

                # Generar el gráfico de barras para las Top-M películas y guardar como imagen
                nombre_imagen = f"{carpeta_imagenes}/top_{m}_peliculas_hasta_{ano}.png"
                self.generar_grafico_barras(top_m_peliculas, criterio, ano, nombre_imagen)

                # Guardar la imagen
                # plt.savefig(nombre_imagen)
                # plt.close()

    def generar_animacion_evolutiva(self, carpeta_imagenes, nombre_gif="animacion_peliculas.gif"):
        # Obtener todas las imágenes generadas en la carpeta
        imagenes = [Image.open(f"{carpeta_imagenes}/{img}") for img in sorted(os.listdir(carpeta_imagenes)) if img.endswith(".png")]

        # Verificar que las imágenes se han cargado correctamente
        if not imagenes:
            print("Error: No se encontraron imágenes para crear el GIF.")
        else:
            print(f"Se encontraron {len(imagenes)} imágenes para la animación.")

        # Guardar las imágenes como un GIF animado
            imagenes[0].save(nombre_gif, save_all=True, append_images=imagenes[1:], optimize=False, duration=500, loop=0)
            print(f"GIF animado creado: {nombre_gif}")


# Uso del código
archivo_csv = '/content/final_dataset.csv'  # Cambiar a la ruta adecuada
taller = Taller3(archivo_csv)

# Carpeta para guardar las imágenes
carpeta_imagenes = "/content/imagenes_peliculas"
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)
    print(f"Carpeta creada: {carpeta_imagenes}")
else:
    print(f"La carpeta ya existe: {carpeta_imagenes}")
taller.solicitar_criterio_m_y_ano()

# Crear animación basada en las imágenes generadas
taller.generar_animacion_evolutiva(carpeta_imagenes)

IPImage(filename='animacion_peliculas.gif')