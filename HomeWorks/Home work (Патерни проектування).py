# Задания по паттернам

# 1 Билдер паттерн

# Сделать так же как мы делали пример с пиццей можно, но было бы
# очень много деталей и код был бы слишком огромным если бы я прописывал все варианты двигателя и цветов.

# import random
#
# class Car:
#     def __init__(self):
#         self.brand = None
#         self.body = None
#         self.color = None
#         self.engine = None
#         self.doors = None
#         self.extra = None
#
#     def __str__(self):
#         return (f"Заказ авто #{random.randint(1000, 9999)}"
#                 f"\n\t Бренд: {self.brand} ({self.body}). \n\t Двигатель: {self.engine}."
#                 f"\n\t Цвет: {self.color}. \n\t Кол-во дверей: {self.doors}. \n\t Дополнительно: {self.extra}."
#                 f"\n Запуск производства.....")
#
# class ConcreteCarBuilder:
#     def __init__(self): self.car = Car()
#     def set_brand(self, brand):
#         self.car.brand = brand
#     def set_body(self, body):
#         self.car.body = body
#     def set_color(self, color):
#         self.car.color = color
#     def set_engine(self, engine):
#         self.car.engine = engine
#     def set_doors(self, doors):
#         self.car.doors = doors
#     def set_extra(self, extra):
#         self.car.extra = extra
#     def get_result(self):
#         return self.car
#
# class Director:
#     def make_tesla(self, builder):
#         builder.set_brand("Tesla")
#         builder.set_body("седан")
#         builder.set_color("белый")
#         builder.set_engine("электрический")
#         builder.set_doors(4)
#         builder.set_extra("автопилот")
#
# builder = ConcreteCarBuilder()
# director = Director()
# director.make_tesla(builder)
# print(builder.get_result())

# 2 Фактори паттерн

from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def get_info(self):
        pass


class Carbonara(Pasta):
    def get_info(self):
        print("\t Ваш заказ: Спагетти\n\t Состав:\n\t\t - Соус сливочный\n\t\t"
              " - Начинка: бекон\n\t\t - Добавки: сыр")

class Bolognese(Pasta):
    def get_info(self):
        print("\t Ваш заказ: Тальятелле\n\t Состав: \n\t\t - Соус томатный\n\t\t"
              " - Начинка: фарш\n\t\t - Добавки: базилик")

class Pesto(Pasta):
    def get_info(self):
        print("\t Ваш заказ: Пенне\n\t Состав: \n\t\t - Соус песто\n\t\t"
              " - Начинка: Кедровые орехи\n\t\t - Добавки: Пармезан")

class PastaFactory:
    def create_pasta(self, pasta_type):
        if pasta_type == "карбонара":
            return Carbonara()
        elif pasta_type == "болоньезе":
            return Bolognese()
        elif pasta_type == "песто":
            return Pesto()
        else:
            raise ValueError("Такой пасты нет в меню")

factory = PastaFactory()
my_pasta = factory.create_pasta("песто")
my_pasta.get_info()


# 3 Сингелтон паттерн

# class Logger:
#     _instance = None
#
#     @staticmethod
#     def get_instance():
#         if Logger._instance is None:
#             Logger._instance = Logger()
#         return Logger._instance
#
#     def log(self, message):
#         print(f"Лог: {message}")
#
#
# nums = [1, 5, 2, 8]
# path = "test.txt"
# logger = Logger.get_instance()
#
#
# mx, mn = max(nums), min(nums)
# logger.log(f"Нашли max: {mx} и min: {mn}")
#
#
# with open(path, "w") as f:
#     f.write(f"{nums}\nMax: {mx}, Min: {mn}")
# logger.log("Все записано в файл")
#
