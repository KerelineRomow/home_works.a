from abc import ABC, abstractmethod

# Я решил использовать DIP
# Начинаю с создания абстрактных классов затребованных инструментов для работы магазина

class Saver(ABC):
    @abstractmethod
    def save(self, items, total):
        pass

class Printer(ABC):
    @abstractmethod
    def print_bill(self, items, total):
        pass


# Создаю класс для прописи кода по сохранению файла
# Так как в дальнейшем заказчик ПО может потребовать изменения способа сохранения
# И как мы и говорили в классе это не должно призвести к поломке всего кода

class FileSaver(Saver):
    def save(self, items, total):
        with open("orders.txt", "a", encoding="utf-8") as f:
            f.write(f"Заказ: {list(items.keys())} | Итого: {total}\n")
        print("Сохранено в файл")

# После сохранения информации, создается видимый чек в консоли

class ConsolePrinter(Printer):
    def print_bill(self, items, total):
        print("--- ЧЕК ---")
        for name, price in items.items():
            print(f"{name}: {price}")
        print(f"ИТОГО К ОПЛАТЕ: {total} грн")
        print("-----------")

# Работа с обсчетом общей стоимости и по условиям акции -10% скидка при покупке товаров
# более чем на 500 грн

class OrderManager:
    def __init__(self, printer, saver):
        self.printer = printer
        self.saver = saver

    def run(self, items):
        total = sum(items.values())
        if total >= 500:
            total = total * 0.9
            print(f"(Применена скидка 10%!)")
        else:
            if total <= 500:
                print()

        self.printer.print_bill(items, total)
        self.saver.save(items, total)


manager = OrderManager(ConsolePrinter(), FileSaver())
order = {"Пицца": 100, "Бургер": 200}
manager.run(order)
