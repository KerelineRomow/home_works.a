import sqlite3

# Использовал деф для красивого и правильного вывода в консоль
# Реализовано автозаполнение таблиц и удаление данных,
# что бы избежать катастрофы в консоли при выводе

conn = sqlite3.connect('sales.db')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS Salesmen(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS Sales(id INTEGER PRIMARY KEY, amount REAL, sid INT, cid INT);
''')

cur.execute("DELETE FROM Sales")
cur.execute("DELETE FROM Salesmen")
cur.execute("DELETE FROM Customers")

cur.executescript('''
INSERT INTO Salesmen VALUES (1,'Иван'),(2,'Анна'),(3,'Олег');
INSERT INTO Customers VALUES (1,'Вектор'),(2,'Петров'),(3,'Альфа');
INSERT INTO Sales(amount, sid, cid) VALUES (5000,1,1),(12000,1,2),(7000,2,1),(3000,3,3),(15000,2,3),(2000,1,1);
''')


def q(text, sql, params=()):
    print(f"\n {text}")
    cur.execute(sql, params)
    res = cur.fetchall()
    for row in res: print(row)

q("1. Все сделки", "SELECT * FROM Sales")
q("2. Сделки Ивана (ID 1)", "SELECT * FROM Sales WHERE sid = 1")
q("3. Максимальная сделка", "SELECT MAX(amount) FROM Sales")
q("4. Минимальная сделка", "SELECT MIN(amount) FROM Sales")
q("5. Макс. сумма Ивана (ID 1)", "SELECT MAX(amount) FROM Sales WHERE sid = 1")
q("6. Мин. сумма Ивана (ID 1)", "SELECT MIN(amount) FROM Sales WHERE sid = 1")
q("7. Макс. сумма Вектора (ID 1)", "SELECT MAX(amount) FROM Sales WHERE cid = 1")
q("8. Мин. сумма Вектора (ID 1)", "SELECT MIN(amount) FROM Sales WHERE cid = 1")

q("9. Продавец с МАКС суммой продаж",
  "SELECT name, SUM(amount) AS s FROM Sales JOIN Salesmen ON sid=Salesmen.id GROUP BY sid ORDER BY s DESC LIMIT 1")

q("10. Продавец с МИН суммой продаж",
  "SELECT name, SUM(amount) AS s FROM Sales JOIN Salesmen ON sid=Salesmen.id GROUP BY sid ORDER BY s ASC LIMIT 1")

q("11. Покупатель с МАКС суммой покупок",
  "SELECT name, SUM(amount) AS s FROM Sales JOIN Customers ON cid=Customers.id GROUP BY cid ORDER BY s DESC LIMIT 1")

q("12. Средний чек Вектора (ID 1)", "SELECT AVG(amount) FROM Sales WHERE cid = 1")
q("13. Средний чек Анны (ID 2)", "SELECT AVG(amount) FROM Sales WHERE sid = 2")

conn.close()
