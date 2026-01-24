import threading
import random
import time
#
# # Задание 1
#
# class MaxFinder(threading.Thread):
#     def __init__(self, numbers):
#         super().__init__()
#         self.numbers = numbers
#
#     def run(self):
#         res = max(self.numbers)
#         print(f"Максимум: {res}")
#
# class MinFinder(threading.Thread):
#     def __init__(self, numbers):
#         super().__init__()
#         self.numbers = numbers
#
#     def run(self):
#         res = min(self.numbers)
#         print(f"Минимум: {res}")
#
# try:
#     user_data = input("Введите числа через пробел: ")
#     my_list = [int(x) for x in user_data.split()]
#
#     if not my_list:
#         print("Список пуст!")
#     else:
#         t1 = MaxFinder(my_list)
#         t2 = MinFinder(my_list)
#
#         t1.start()
#         t2.start()
#
#         t1.join()
#         t2.join()
#
# except ValueError:
#     print("Ошибка: Вводите только целые числа через пробел")
#
#
# # Задание 2
#
# # !Не совсем понял про пути к файлу и реализовал ввод названия файла который лежит в той же
# # дериктории где и сам файл пайтон!
#
# class EvenSaver(threading.Thread):
#     def __init__(self, numbers):
#         super().__init__()
#         self.numbers = numbers
#
#     def run(self):
#         evens = [str(n) for n in self.numbers if n % 2 == 0]
#         with open("even.txt", "w") as f:
#             f.write(" ".join(evens))
#         print(f"Четных найдено: {len(evens)}")
#
# class OddSaver(threading.Thread):
#     def __init__(self, numbers):
#         super().__init__()
#         self.numbers = numbers
#
#     def run(self):
#         odds = [str(n) for n in self.numbers if n % 2 != 0]
#         with open("odd.txt", "w") as f:
#             f.write(" ".join(odds))
#         print(f"Нечетных найдено: {len(odds)}")
#
# try:
#     filename = input("Введите название файла с числами: ")
#
#     if not filename:
#         print("Файл пуст")
#     else:
#         with open(filename, "r") as f:
#             data = [int(x) for x in f.read().split()]
#
#         if not data:
#             print("В файле нет чисел!")
#         else:
#             t1 = EvenSaver(data)
#             t2 = OddSaver(data)
#
#             t1.start()
#             t2.start()
#
#             t1.join()
#             t2.join()
#             print("Готово! Файлы even.txt и odd.txt созданы")
#
# except FileNotFoundError:
#     print(f"Ошибка: Файла '{filename}' не найден")
# except ValueError:
#     print("Ошибка: В файле должны быть только числа")
#
#
# # Задание 3
#
# class WordSearcher(threading.Thread):
#     def __init__(self, filename, word):
#         super().__init__()
#         self.filename = filename
#         self.word = word
#
#     def run(self):
#         with open(self.filename, "r", encoding="utf-8") as f:
#             content = f.read()
#             if self.word in content:
#                 print(f"\n[Результат]: Слово '{self.word}' найдено!")
#             else:
#                 print(f"\n[Результат]: Слово '{self.word}' НЕ найдено.")
#
# try:
#     file_name = input("Введите название файла для поиска (например, test.txt): ")
#     search_word = input("Введите слово, которое нужно найти: ")
#
#     if not file_name or not search_word:
#         print("Ошибка: Нужно ввести и название файла, и слово!")
#     else:
#         t = WordSearcher(file_name, search_word)
#         t.start()
#         t.join()
# except Exception as e:
#     print(e)
#
#
# # 4 задание
#
# shared_list = []
# data_ready = threading.Event()
#
# class ListFiller(threading.Thread):
#     def run(self):
#         global shared_list
#         print("Поток 1: Начинаю генерацию чисел...")
#         shared_list = [random.randint(1, 100) for _ in range(10)]
#         time.sleep(2)
#         print(f"Поток 1: Список готов: {shared_list}")
#         data_ready.set()
#
#
# class SumWorker(threading.Thread):
#     def run(self):
#         print("Поток 2: Жду готовности списка...")
#         data_ready.wait()
#         s = sum(shared_list)
#         print(f"Поток 2: Сумма всех чисел = {s}")
#
#
# class AvgWorker(threading.Thread):
#     def run(self):
#         print("Поток 3: Жду готовности списка...")
#         data_ready.wait()
#
#         avg = sum(shared_list) / len(shared_list)
#         print(f"Поток 3: Среднее арифметическое = {avg}")
#
# t1 = ListFiller()
# t2 = SumWorker()
# t3 = AvgWorker()
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# print("\nВсе задачи выполнены!")