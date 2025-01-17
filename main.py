from random import *
import random
from faker import Faker
fake = Faker()
#from datetime import datetime
import datetime

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        #Variables
        self.watch_counts = 5
        self.type = "movie"
    def __str__(self):
        return f'{self.genre} "{self.title}" wydany w roku {self.year}, oglądano {self.watch_counts} razy'
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
        return f'{self.genre} "{self.title}" wydany w roku {self.year}, sezon {self.season_number}, odcinek {self.episode_number}, oglądano {self.watch_counts} razy'
    def play(self):
        self.watch_counts += 1
        print(f'Oglądasz serial: "{self.title} S{str(self.season_number).zfill(2)}E{str(self.episode_number).zfill(2)}"')

def Generate_Movies_Series():   #wypełnienie biblioteki filmów danymi
    MovieGenres = ["Komedia", "Dramat", "Melodramat", "Western", "Horror", "Musical", "Thriller", "Film sensacyjny", "Kryminał", "Film SF", "Film fantasy", "Film historyczny", "Film psychologiczny", "Film wojenny", "Film familijny"]
    #ręczne tworzenie filmów/seriali i dodanie do listy
    movie1 = Movie(title="Akademia Pana Kleksa", year=2024, genre="Film familijny")
    movie2 = Movie(title="Matrix", year=1999, genre="Film SF")
    series1 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=1)
    series2 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=2)
    series3 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=3)
    series4 = Series(title="Czarnobyl", year=2019, genre="Dramat", season_number=1, episode_number=4)
    Library = [movie1, movie2, series1, series2, series3, series4]
    #tworzenie filmów i dodanie do listy
    for i in range(0,50):
        movie = Movie(title=fake.bs().title(), year=randint(1950,2025), genre=random.choice(MovieGenres))
        Library.append(movie)
    #tworzenie seriali i dodanie do listy
    for i in range(0,50):   #liczba seriali
        jj = randint(1,8)   #losowa liczba sezonów
        kk = randint(6,12)    #losowa liczba odcinków w sezonie, w każdym sezonie taka sama liczba odcinków
        title_temp=fake.bs().title()
        year_temp = randint(1980,2025)
        genre_temp = random.choice(MovieGenres)
        for j in range(1, jj):
            for k in range(1, kk):
                series = Series(title=title_temp, year=year_temp, genre=genre_temp, season_number=j, episode_number=k)
                Library.append(series)
    return Library

def view_Library(LibraryAll, content_type):
    if content_type == "movie":
        print("Wszystkie filmy w bibliotece: ")
    if content_type == "series":
        print("Wszystkie seriale w bibliotece: ")
    for movie_series in LibraryAll:
        if content_type == "movie" and movie_series.type == "movie":
            print(movie_series)
        elif content_type == "series" and movie_series.type == "series":
            print(movie_series)

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

def episodes_number(LibraryAll):
    episodes = []
    for series in LibraryAll:
        if series.type == "series":
            episodes.append(series)
    episodes_number = {}
    for episod in episodes: # tworzy słownik z tytułem i zerową ilością wystąpień
        episodes_number[episod.title] = 0
    for episod in episodes:    
        if episod.title in episodes_number:     #iteruje listę, jeśli znajdzie tytuł występujący w słowniku to +1, jeśli nie to rozpoczyna odliczanie =1
            episodes_number[episod.title] += 1 
        else:
            episodes_number[episod.title] = 1
    print("Serial i liczba wszystkich odcinków: ")
    for key, value in episodes_number.items():
        print(f"Serial {key} posiada {value} odcinków")

def search(LibraryAll):
    search_title_list = []
    search_title=input("Podaj tytuł, który chcesz znaleźć:")
    print("Znalezione pozycje: ")
    for movie_series in LibraryAll:
        if search_title.lower() == movie_series.title.lower():
            print(movie_series)
            search_title_list.append(movie_series)
    return search_title_list

def generate_views(LibraryAll):
    random_movie = randint(0, len(LibraryAll)-1)
    #do testów: 
    #print(f"Losowy film: {LibraryAll[random_movie]}, pooglądano {LibraryAll[random_movie].watch_counts} razy")
    LibraryAll[random_movie].watch_counts += randint(1,100)
    #do testów: 
    #print(f"Losowy film {LibraryAll[random_movie]} po funkcji 'generate_view' pooglądano: {LibraryAll[random_movie].watch_counts} razy")

def generate_views_x10(LibraryAll):
    for i in range(0,10):
        generate_views(LibraryAll)

""" #funkcja niewykorzystywana, pierwsza wersja, wyświetla tylko TOP1
def top_titles(LibraryAll):     
    top_movie_count = 0
    top_list = []
    for movie in LibraryAll:
        if movie.watch_counts >= top_movie_count:
            top_movie_count = movie.watch_counts
            top_movie = movie
    for movie in LibraryAll:
        if movie.watch_counts == top_movie_count:
            top_list.append(movie)
    print(f"\nNajchętniej oglądane filmy i seriale: ")
    for i in range(0,len(top_list)):
        print(f"{top_list[i]}, oglądano: {top_list[i].watch_counts}")
    return top_list
"""

def top_titles(LibraryAll, how_many):   #najpopularniejsze filmy i seriale ze wskazaniem ilości
    top_list = []
    sorted_list = sorted(LibraryAll, key=lambda Movie: Movie.watch_counts, reverse=True)
    for item in sorted_list:
        if item.watch_counts >= sorted_list[how_many-1].watch_counts:
            top_list.append(item)
    today = datetime.date.today()
    print(f"\nTOP{how_many} Najpopularniejsze filmy i seriale obecnie, tj. {today}: ")
    for top in top_list:
        print(top)

#TESTY:
#view_Library(LibraryMoviesSeries, "series")
#view_Library(LibraryMoviesSeries, "movie") 
#get_movies(LibraryMoviesSeries)     #wyświetlenie filmów alfabetycznie
#get_series(LibraryMoviesSeries)     #wyświetlenie seriali alfabetycznie
#search(LibraryMoviesSeries)    #wyszukiwanie filmu po nazwie
#generate_view_x10(LibraryMoviesSeries) #generowanie wyświetleń
#top_titles(LibraryMoviesSeries, 5) #najpopularniejsze filmy, TOP_X
#episodes_number(LibraryMoviesSeries)   #sumowanie odcinków seriali

print("\nBIBLIOTEKA FILMÓW\n")
LibraryMoviesSeries = Generate_Movies_Series()  #wypełnienie biblioteki
generate_views_x10(LibraryMoviesSeries)
generate_views_x10(LibraryMoviesSeries)
episodes_number(LibraryMoviesSeries)
top_titles(LibraryMoviesSeries, 3)

