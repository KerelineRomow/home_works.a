from abc import ABC, abstractmethod, ABCMeta

# Задание 1


class Transport(ABC):
    @abstractmethod

    def move (self):
        pass

    def info (self):
        print("This is a vehicle designed for travel.")

class Car(Transport):
    def move (self):
        print("Car is now moving.\n")

class Bicycle(Transport):
    def move (self):
        print("Bicycle is turning the corner.\n")

class Train(Transport):
    def move (self):
        print("Train is now moving on the rails.\n")

vehicles = [Car(), Bicycle(), Train()]

for transport in vehicles:
    transport.info()
    transport.move()


# Задание 2


class ValidationMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        if "description" not in dct:
            dct["description"] = "Default description"
        elif not isinstance(dct["description"], str):
            raise ValueError("description must be a string")

        for key, value in dct.items():
            if callable(value) and not key.startswith("__"):
                if not key.startswith("do_"):
                    raise ValueError(f"Method {key} must start with 'do_'!")

        return super().__new__(cls, name, bases, dct)


class ValidatedClass(ABC, metaclass=ValidationMeta):
    pass


try:
    class TestClGood(ValidatedClass):
        description = "Я соблюдаю правила"

        def do_work(self):
            pass

    print("Успех: TestClGood создан!")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    class TestClNotdescription(ValidatedClass):


        def do_work(self):
            pass

    print("Успех: TestClGood создан!")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    class TestCl2Bad(ValidatedClass):
        def work_wrong(self):
            pass

except ValueError as e:
    print(f"Ошибка: {e}")

