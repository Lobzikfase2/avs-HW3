from generator import gen_str
from random import randint


class Film:
    __film_type = None
    __title = None
    __year = None
    __special_argument = None

    def __init__(self, film_type: str, title: str, year: str, something: tuple):
        self.__film_type = film_type
        self.__title = title
        self.__year = year
        self.__special_argument = something

    def __str__(self):
        data = ""
        data += self.__film_type + '\n'
        data += "\ttitle: " + self.__title + '\n'
        data += "\tyear: " + self.__year + '\n'
        data += "\t" + self.__special_argument[0] + ": " + self.__special_argument[1] + '\n'
        data += '\n'
        return data

    @staticmethod
    def gen_film():
        film_type = randint(1, 3)
        if film_type == 1:
            film_type = "Feature film"
            something = ("director", gen_str() + " " + gen_str())
        elif film_type == 2:
            animation_type = randint(1, 3)
            if animation_type == 1:
                something = ("type", "hand drawn")
            elif animation_type == 2:
                something = ("type", "puppet")
            else:
                something = ("type", "plasticine")
            film_type = "Cartoon film"
        else:
            film_type = "Documentary film"
            something = ("duration", str(randint(60, 210)))
        title = gen_str()
        year = str(randint(1895, 2021))
        film = Film(film_type, title, year, something)
        return film

    def func(self):
        return int(self.__year) / len(self.__title.strip())
