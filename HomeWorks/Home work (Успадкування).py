# Задание 1
class Passport:
    def __init__(self, full_name="", date_of_birth="", country=""):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.country = country

    def input_data(self):
        print("\n--- Ввод данных паспорта ---")
        self.full_name = input("Введите ФИО: ")
        self.date_of_birth = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        self.country = input("Введите страну: ")

    def get_info(self):
        return (f"Тип: Паспорт гражданина\n"
                f"ФИО: {self.full_name}\n"
                f"Дата рождения: {self.date_of_birth}\n"
                f"Страна: {self.country}")

class ForeignPassport(Passport):
    def __init__(self, full_name="", date_of_birth="", country="", fp_number="", visas=""):
        super().__init__(full_name, date_of_birth, country)
        self.fp_number = fp_number
        self.visas = visas

    def input_data(self):
        super().input_data()
        print("\n--- Дополнительные данные загранпаспорта ---")
        self.fp_number = input("Введите номер загранпаспорта: ")
        self.visas = input("Введите список виз через запятую: ")

    def get_info(self):
        return (f"Тип: Заграничный паспорт\n"
                f"ФИО: {self.full_name}\n"
                f"Дата рождения: {self.date_of_birth}\n"
                f"Страна: {self.country}\n"
                f"Номер загранпаспорта: {self.fp_number}\n"
                f"Визы: {self.visas}")

# fp = ForeignPassport()
# fp.input_data()
# print("\nИнформация о загранпаспорте:")
# print(fp.get_info())

# Задание 2

class Device:
    def __init__(self, name="", manufacturer="", power_w=0):
        self.name = name
        self.manufacturer = manufacturer
        self.power_w = power_w

    def input_data(self):
        try:
            print(f"\n--- Ввод данных о {self.name} ---")
            self.manufacturer = input("Введите производителя: ")
            self.power_w = int(input("Введите мощность (Вт): "))
        except ValueError:
            print("Ошибка! Мощность должна быть целым числом.")
            raise

    def get_info(self):
        return (f"Тип устройства: {self.name}\n"
                f"Производитель: {self.manufacturer}\n"
                f"Мощность: {self.power_w} Вт")

class CoffeeMachine(Device):
    def __init__(self, manufacturer="", power_w=0, water_tank_l=0.0):
        super().__init__("Кофемашина", manufacturer, power_w)
        self.water_tank_l = water_tank_l

    def input_data(self):
        super().input_data()
        try:
            self.water_tank_l = float(input("Введите объем резервуара для воды (л): "))
        except ValueError:
            print("Ошибка! Объем должен быть числом.")
            raise

    def get_info(self):
        return (super().get_info() +
                f"\nОбъем резервуара: {self.water_tank_l} л")

class Blender(Device):
    def __init__(self, manufacturer="", power_w=0, speed_levels=0):
        super().__init__("Блендер", manufacturer, power_w)
        self.speed_levels = speed_levels

    def input_data(self):
        super().input_data()
        try:
            self.speed_levels = int(input("Введите количество скоростей: "))
        except ValueError:
            print("Ошибка! Количество скоростей должно быть целым числом.")
            raise

    def get_info(self):
        return (super().get_info() +
                f"\nКоличество скоростей: {self.speed_levels}")

class MeatGrinder(Device):
    def __init__(self, manufacturer="", power_w=0, reverse_mode=False):
        super().__init__("Мясорубка", manufacturer, power_w)
        self.reverse_mode = reverse_mode

    def input_data(self):
        super().input_data()
        reverse = input("Есть ли режим реверса (да/нет)?: ").lower()
        self.reverse_mode = (reverse == 'да' or reverse == 'yes')

    def get_info(self):
        reverse_status = "да" if self.reverse_mode else "нет"
        return (super().get_info() +
                f"\nРежим реверса: {reverse_status}")

# coffee_machine = CoffeeMachine()
# coffee_machine.input_data()
# print("\nИнформация о кофемашине:")
# print(coffee_machine.get_info())

# blender = Blender()
# blender.input_data()
# print("\nИнформация о блендере:")
# print(blender.get_info())

# meat_grinder = MeatGrinder()
# meat_grinder.input_data()
# print("\nИнформация о мясорубке:")
# print(meat_grinder.get_info())

# Задание 3

class Ship:
    def __init__(self, name="", displacement_t=0, class_type="Корабль"):
        self.name = name
        self.displacement_t = displacement_t
        self.class_type = class_type

    def input_data(self):
        try:
            print(f"\n--- Ввод данных о {self.class_type} ---")
            self.name = input("Введите название корабля: ")
            self.displacement_t = int(input("Введите водоизмещение (тонн): "))
        except ValueError:
            print("Ошибка! Водоизмещение должно быть целым числом.")
            raise

    def get_info(self):
        return (f"Класс: {self.class_type}\n"
                f"Название: {self.name}\n"
                f"Водоизмещение: {self.displacement_t:} т")

class Frigate(Ship):
    def __init__(self, name="", displacement_t=0, missile_cells=0):
        super().__init__(name, displacement_t, "Фрегат")
        self.missile_cells = missile_cells

    def input_data(self):
        super().input_data()
        try:
            self.missile_cells = int(input("Введите количество ракетных ячеек: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            raise

    def get_info(self):
        return (super().get_info() +
                f"\nРакетные ячейки: {self.missile_cells}")

class Destroyer(Ship):
    def __init__(self, name="", displacement_t=0, main_gun_caliber_mm=0):
        super().__init__(name, displacement_t, "Эсминец")
        self.main_gun_caliber_mm = main_gun_caliber_mm

    def input_data(self):
        super().input_data()
        try:
            self.main_gun_caliber_mm = int(input("Введите калибр главного орудия (мм): "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            raise

    def get_info(self):
        return (super().get_info() +
                f"\nКалибр главного орудия: {self.main_gun_caliber_mm} мм")

class Cruiser(Ship):
    def __init__(self, name="", displacement_t=0, aircraft_capacity=0):
        super().__init__(name, displacement_t, "Крейсер")
        self.aircraft_capacity = aircraft_capacity

    def input_data(self):
        super().input_data()
        try:
            self.aircraft_capacity = int(input("Введите вместимость летательных аппаратов: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            raise

    def get_info(self):
        return (super().get_info() +
                f"\nВместимость ЛА: {self.aircraft_capacity}")


# frigate = Frigate()
# frigate.input_data()
# print("\Информация о фрегате:")
# print(frigate.get_info())

# destroyer = Destroyer()
# destroyer.input_data()
# print("\Информация о эсминце:")
# print(destroyer.get_info())
#
# cruiser = Cruiser()
# cruiser.input_data()
# print("\Информация о крейсере:")
# print(cruiser.get_info())

# Задание 5

class TemperatureConverter:

    _calculation_count = 0

    @staticmethod
    def _increment_count():
        TemperatureConverter._calculation_count += 1

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter._increment_count()
        fahrenheit = celsius * 9 / 5 + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter._increment_count()
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    @staticmethod
    def get_calculation_count():
        return TemperatureConverter._calculation_count

    @staticmethod
    def run_converter():
        print("\n--- Конвертер температуры ---")
        try:
            celsius_input = input("Введите температуру в Цельсиях (C): ")
            fahrenheit_input = input("Введите температуру в Фаренгейтах (F): ")
            temp_c = float(celsius_input)
            temp_f = float(fahrenheit_input)
            f_result = TemperatureConverter.celsius_to_fahrenheit(temp_c)
            c_result = TemperatureConverter.fahrenheit_to_celsius(temp_f)
            print(f"\nКонвертация C -> F: {temp_c:.2f}°C = {f_result:.2f}°F")
            print(f"Конвертация F -> C: {temp_f:.2f}°F = {c_result:.2f}°C")

        except ValueError:
            print("Ошибка ввода! Пожалуйста, вводите только числа.")

        count = TemperatureConverter.get_calculation_count()
        print(f"\nВсего выполнено конвертаций: {count}")

# TemperatureConverter.run_converter()

# Задание 6

class LengthConverter:

    _meters_in_foot = 0.3048
    _feet_in_meter = 1 / _meters_in_foot

    _calculation_count = 0

    @staticmethod
    def _increment_count():
        LengthConverter._calculation_count += 1

    @staticmethod
    def meters_to_feet(meters):
        LengthConverter._increment_count()
        feet = meters * LengthConverter._feet_in_meter
        return feet

    @staticmethod
    def feet_to_meters(feet):
        LengthConverter._increment_count()
        meters = feet * LengthConverter._meters_in_foot
        return meters

    @staticmethod
    def get_calculation_count():
        return LengthConverter._calculation_count

    @staticmethod
    def run_converter():
        print("\n--- Конвертер длины ---")
        try:
            meters_input = input("Введите длину в метрах (m): ")
            feet_input = input("Введите длину в футах (ft): ")
            length_m = float(meters_input)
            length_ft = float(feet_input)
            feet_result = LengthConverter.meters_to_feet(length_m)
            meters_result = LengthConverter.feet_to_meters(length_ft)
            print(f"\nКонвертация Метры -> Футы: {length_m} м = {feet_result} фт")
            print(f"Конвертация Футы -> Метры: {length_ft} фт = {meters_result} м")

        except ValueError:
            print("Ошибка ввода! Пожалуйста, вводите только числа.")

        count = LengthConverter.get_calculation_count()
        print(f"\nВсего выполнено конвертаций длины: {count}")


# LengthConverter.run_converter()


