from film import Film


class Container:
    __films_list = []
    __function_average = None

    def read_films_from_file(self, path: str):
        self.__films_list.clear()
        with open(path, "r", encoding="UTF-8") as file:
            while True:
                read_type = file.readline().strip()
                if read_type not in ["1", "2", "3"]:
                    break
                title = file.readline().strip()
                year = file.readline().strip()
                if read_type == "1":
                    film_type = "Feature film"
                    special_argument = ("director", file.readline().strip())
                elif read_type == "2":
                    film_type = "Cartoon film"
                    animation_type = file.readline().strip()
                    if animation_type == "1":
                        special_argument = ("type", "hand drawn")
                    elif animation_type == "2":
                        special_argument = ("type", "puppet")
                    else:
                        special_argument = ("type", "plasticine")
                else:
                    film_type = "Documentary film"
                    special_argument = ("duration", file.readline().strip())
                film = Film(film_type, title, year, special_argument)
                self.__films_list.append(film)

    def generate_films_list(self, count: int):
        self.__films_list.clear()
        for i in range(count):
            self.__films_list.append(Film.gen_film())

    def write_films_to_file(self, path: str):
        with open(path, "w", encoding="UTF-8") as file:
            if self.__function_average:
                file.write(f"Function result: {round(self.__function_average, 2)}.\n")
            file.write(f"Container contains {len(self.__films_list)} elements.\n\n")
            for film in self.__films_list:
                file.write(str(film))

    def delete_elements(self):
        _sum = 0.0
        for film in self.__films_list:
            _sum += film.func()
        self.__function_average = _sum / len(self.__films_list)
        for film in self.__films_list:
            if film.func() < self.__function_average:
                self.__films_list.remove(film)
