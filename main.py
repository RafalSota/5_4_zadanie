from random import *
import random
from faker import Faker
fake = Faker()
from datetime import datetime

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        #Variables
        self.watch_counts = 5
        self.type = "movie"
    def __str__(self):
        return f'{self.genre} "{self.title}" wydany w roku {self.year}'
    def play(self):
        self.watch_counts += 1
        print(f'Oglądasz film: "{self.title} ({self.year})"')
class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
        self.type = "series"
    def __str__(self):
        return f'{self.genre} "{self.title}" wydany w roku {self.year}, sezon {self.season_number}, odcinek {self.episode_number}'
    def play(self):
        self.watch_counts += 1
        print(f'Oglądasz serial: "{self.title} S{str(self.season_number).zfill(2)}E{str(self.episode_number).zfill(2)}"')

LibraryMovies = []

def Generate_Movies_Series():   #wypełnienie biblioteki filmów danymi
    MovieGenres = ["Komedia", "Dramat", "Melodramat", "Western", "Horror", "Musical", "Thriller", "Film sensacyjny", "Kryminał", "Film SF", "Film fantasy", "Film historyczny", "Film psychologiczny", "Film wojenny", "Film familijny"]
    #ręczne tworzenie filmów/seriali i dodanie do listy
    movie1 = Movie(title="Akademia Pana Kleksa", year=2024, genre="Film familijny")
    series1 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=1)
    series2 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=2)
    series3 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=3)
    series4 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=4)
    Library = [movie1, series1, series2, series3, series4]
    #tworzenie filmów i dodanie do listy
    for i in range(1,50):
        movie = Movie(title=fake.bs().title(), year=randint(1950,2025), genre=random.choice(MovieGenres))
        Library.append(movie)
    #tworzenie seriali i dodanie do listy
    for i in range(1,30):   #liczba seriali
        jj = randint(1,8)   #liczba sezonów
        kk = randint(6,12)    #liczba odcinków w sezonie
        title_temp=fake.bs().title()
        year_temp = randint(1980,2025)
        genre_temp = random.choice(MovieGenres)
        for j in range(1, jj):
            for k in range(1, kk):
                series = Series(title=title_temp, year=year_temp, genre=genre_temp, season_number=j, episode_number=k)
                Library.append(series)
    return Library

def get_movies(LibraryAll):
    LibraryMovies = []
    for movie in LibraryAll:
        if movie.type == "movie":
            LibraryMovies.append(movie)
    movies_by_title = sorted(LibraryMovies, key=lambda Movie: Movie.title)
    print("\nFilmy pełnometrażowe w naszej bibliotece posortowane według tytułu:")
    for movie in movies_by_title:
        print(movie)
    return LibraryMovies

def get_series(LibraryAll):
    LibrarySeries = []
    for series in LibraryAll:
        if series.type == "series":
            LibrarySeries.append(series)
    series_by_title=sorted(LibrarySeries, key=lambda Series: Series.title)
    print("\nSeriale w naszej bibliotece posortowane według tytułu:")
    for series in series_by_title:
        print(series)
    return LibrarySeries

LibraryMoviesSeries = Generate_Movies_Series()  #wypełnienie biblioteki
for movie_series in LibraryMoviesSeries:        #wyświetlenie biblioteki
    print(movie_series)

get_movies(LibraryMoviesSeries)     #wyświetlenie filmów alfabetycznie
get_series(LibraryMoviesSeries)     #wyświetlenie seriali alfabetycznie
