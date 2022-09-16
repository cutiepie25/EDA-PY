import csv


class Pelicula:

    def __init__(self, imdb_title_id:str, title:str, original_title:str, year:int, 
    date_published:str, genre:str, duration:int, country:str, language:str, director:str, 
    writer:str, production_company:str, actors:str, description:str, avg_vote:float,
    votes:int, budget:str, usa_gross_income:str, worlwide_gross_income:str, 
    metascore:str, reviews_from_users:float, reviews_from_critics:str):

        self.imdb_title_id = imdb_title_id;
        self.title = title
        self.original_title = original_title
        self.year = year
        self.date_published = date_published
        self.genre = genre
        self.duration = duration
        self.country = country
        self.language = language
        self.director = director
        self.writer = writer
        self.production_company = production_company
        self.actors = actors
        self.description = description
        self.avg_vote = avg_vote
        self.votes = votes
        self.budget = budget
        self.usa_gross_income = usa_gross_income
        self.worlwide_gross_income = worlwide_gross_income
        self.metascore = metascore
        self.reviews_from_users = reviews_from_users
        self.reviews_from_critics = reviews_from_critics

    def __str__(self):
        return f"{self.title} , {self.avg_vote}"


def read_csv(filename):
    pelis = []
    with open(filename) as fh:
        reader = csv.reader(fh, delimiter=',', quotechar='"')
        for rec in reader:
            try:
                pelicula = Pelicula(
                    rec[0],
                    rec[1],
                    rec[2],
                    int(rec[3]),
                    rec[4],
                    rec[5],
                    int(rec[6]),
                    rec[7],
                    rec[8],
                    rec[9],
                    rec[10],
                    rec[11],
                    rec[12],
                    rec[13],
                    float(rec[14]),
                    int(rec[15]),
                    rec[16],
                    rec[17],
                    rec[18],
                    rec[19],
                    rec[20],
                    rec[21]
                )
                pelis.append(pelicula)
            except:
                print('ERROR')
    return pelis


if __name__=="__main__":
    peliculas = read_csv('/hdd/home/jmlon/tmp/Datasets/IMDb movies.csv')
    for i in range(10):
        print(peliculas[i])

