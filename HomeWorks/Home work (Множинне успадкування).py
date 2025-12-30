# Задание 1


class Film:
    all_films = []

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        Film.all_films.append(self)

    @classmethod
    def average_rating(cls):
        if not cls.all_films:
            return 0
        total_rating = sum(film.rating for film in cls.all_films)
        return total_rating / len(cls.all_films)

    @staticmethod
    def show_ratings():
        print("Рейтинги всех фильмов:")
        for film in Film.all_films:
            print(f"{film.name}: {film.rating}")

    @staticmethod
    def show_names():
        print("Названия всех фильмов:")
        for film in Film.all_films:
            print(film.name)

# f1 = Film("Inception", 9)
# f2 = Film("Interstellar", 10)
# f3 = Film("The Dark Knight", 8)
#
# Film.show_names()
# Film.show_ratings()
# print(f"\nСредний рейтинг всех фильмов: {Film.average_rating():.2f}")


# Задание 2

class Brain:
    def think(self):
        return "Мышление"

class Heart:
    def beat(self):
        return "Сердце бьется"

class Legs:
    def walk(self):
        return "Ходьба"

class Person(Brain, Heart, Legs):
    def __init__(self, name):
        self.name = name

    def status(self):
        print(f"Name: {self.name}")
        print(self.think())
        print(self.beat())
        print(self.walk())

# human = Person("Roman")
# human.status()


# Задание 3

class Instrument:
    def play(self):
        pass


class StringInstrument(Instrument):
    def play(self):
        print("Звучит струнный инструмент")


class WindInstrument(Instrument):
    def play(self):
        print("Звучит духовой инструмент")


class PercussionInstrument(Instrument):
    def play(self):
        print("Звучит ударный инструмент")


class Guitar(StringInstrument):
    def play(self):
        print("Гитара играет")

    def tune(self):
        print("Гитара настроена")


class Flute(WindInstrument):
    def play(self):
        print("Флейта играет")

    def twists(self):
        print("Флейта собрана")


class Drum(PercussionInstrument):
    def play(self):
        print("Барабан играет")

    def build(self):
        print("Барабан установлен")


guitar = Guitar()
flute = Flute()
drum = Drum()

guitar.tune()
guitar.play()
flute.twists()
flute.play()
drum.build()
drum.play()


class HybridInstrument(StringInstrument, WindInstrument, PercussionInstrument):
    def play(self):
        print("Гибридный инструмент сочетает звуки:")
        StringInstrument.play(self)
        WindInstrument.play(self)
        PercussionInstrument.play(self)


hybrid = HybridInstrument()
hybrid.play()