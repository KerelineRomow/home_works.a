# Задание 1

class Human:
    def __init__(self, name="", family_name="", father_name="",
                 b_year=0, phone_num="", city="", country="", home_adress=""):
        self.name = name
        self.family_name = family_name
        self.father_name = father_name
        self.b_year = b_year
        self.phone_num = phone_num
        self.city = city
        self.country = country
        self.home_adress = home_adress

    def enter_info(self):
        try:
            self.name = input("Введите имя: ")
            self.family_name = input("Введите фамилию: ")
            self.father_name = input("Введите отчество: ")
            self.b_year = int(input("Введите год рождения: "))
            self.phone_num = input("Введите телефон: ")
            self.city = input("Введите город: ")
            self.country = input("Введите страну: ")
            self.home_adress = input("Введите домашний адрес: ")
        except ValueError:
            print("Ошибка! Введите целое число (год рождения).")
            raise

    def is_major(self):
        try:
            if self.b_year == 0:
                return False
            elif 2025 - self.b_year >= 18:
                return True
            else:
                return False
        except ValueError:
            return False

    def show_human_card(self):
        return (f"ФИО: {self.family_name} {self.name} {self.father_name}\n"
            f"Год рождения: {self.b_year}\n"
            f"Телефон: {self.phone_num}\n"
            f"Город: {self.city}\n"
            f"Страна: {self.country}\n"
            f"Адрес: {self.home_adress}")

# person = Human()
# person.enter_info()
# print("\nСовершеннолетний:", person.is_major())
# print("\nИнформация о человеке:")
# print(person.show_human_card())


# Задание 2

class City:
    def __init__(self, name="", region="", country="", population=0, zipcode="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipcode = zipcode
        self.phone_code = phone_code

    def input_data(self):
        try:
            self.name = input("Введите название города: ")
            self.region = input("Введите регион: ")
            self.country = input("Введите страну: ")
            self.population = int(input("Введите количество жителей: "))
            self.zipcode = input("Введите почтовый индекс: ")
            self.phone_code = input("Введите телефонный код: ")
        except ValueError:
            print("Ошибка! Введите целое число для населения.")
            raise

    def get_info(self):
        return (f"Город: {self.name}\n"
                f"Регион: {self.region}\n"
                f"Страна: {self.country}\n"
                f"Население: {self.population}\n"
                f"Почтовый индекс: {self.zipcode}\n"
                f"Телефонный код: {self.phone_code}")

    def is_valid_zipcode(self):
        if 5 <= len(self.zipcode) <= 5:
            print(f"{self.zipcode} правильный")
            return True
        else:
            print("\n\tВведен не верный почтовый индекс!")
            return False


# city1 = City()
# city1.input_data()
# print("\nИнформация о городе:")
# print(city1.get_info())
# print(city1.is_valid_zipcode())

# Задание 3

class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=""):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def input_data(self):
        try:
            self.name = input("Введите название страны: ")
            self.continent = input("Введите название континента: ")
            self.population = int(input("Введите количество жителей (целое число): "))
            self.phone_code = input("Введите телефонный код страны: ")
            self.capital = input("Введите название столицы: ")
            self.cities = input("Введите названия городов через запятую: ")
        except ValueError:
            print("Ошибка! Введите целое число для населения.")
            raise

    def get_info(self):
        return (f"Страна: {self.name}\n"
                f"Континент: {self.continent}\n"
                f"Население: {self.population:,}\n"
                f"Телефонный код: {self.phone_code}\n"
                f"Столица: {self.capital}\n"
                f"Города: {self.cities}")


# country1 = Country()
# country1.input_data()
# print("\nИнформация о стране:")
# print(country1.get_info())

# Задание 4

class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        try:
            self.model = input("Введите название модели: ")
            self.year = int(input("Введите год выпуска (целое число): "))
            self.manufacturer = input("Введите производителя: ")
            self.engine_volume = float(input("Введите объем двигателя (напр., 2.0): "))
            self.color = input("Введите цвет машины: ")
            self.price = int(input("Введите цену: "))
        except ValueError:
            print("Ошибка! Проверьте, что год и цена — целое число, а объем — число с точкой.")
            raise

    def get_info(self):
        return (f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n"
                f"Производитель: {self.manufacturer}\n"
                f"Объем двигателя: {self.engine_volume} л\n"
                f"Цвет: {self.color}\n"
                f"Цена: {self.price} USD")

# car1 = Car()
# car1.input_data()
# print("\nИнформация об автомобиле:")
# print(car1.get_info())

# Задание 5

class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        try:
            self.title = input("Введите название книги: ")
            self.year = int(input("Введите год издания (целое число): "))
            self.publisher = input("Введите издателя: ")
            self.genre = input("Введите жанр: ")
            self.author = input("Введите автора: ")
            self.price = float(input("Введите цену (напр., 15.99): "))
        except ValueError:
            print("Ошибка! Проверьте, что год — целое число, а цена — число с точкой.")
            raise

    def get_info(self):
        return (f"Название: {self.title}\n"
                f"Автор: {self.author}\n"
                f"Год издания: {self.year}\n"
                f"Издатель: {self.publisher}\n"
                f"Жанр: {self.genre}\n"
                f"Цена: {self.price}")

# book1 = Book()
# book1.input_data()
# print("\nИнформация о книге:")
# print(book1.get_info())


