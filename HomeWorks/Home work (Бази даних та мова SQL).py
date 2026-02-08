import sqlite3

# Задание 1

def main():
    conn = sqlite3.connect('students_grades.db')
    conn.execute('PRAGMA foreign_keys=ON;')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS StudentGrades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        birth_date TEXT,
        email TEXT,
        phone TEXT,
        group_name TEXT,
        avg_yearly_grade REAL,
        min_grade_subject TEXT,
        max_grade_subject TEXT
    )
    ''')

    cursor.execute("DELETE FROM StudentGrades")

    cursor.execute('''
    INSERT INTO StudentGrades (
        full_name, city, country, birth_date, email, phone,
        group_name, avg_yearly_grade, min_grade_subject, max_grade_subject
    ) VALUES (
        'Иванов Иван Иванович', 'Киев', 'Украина', '2005-05-15',
        'ivanov@example.com', '+380991234567', 'П-11', 10.5, 'Физика', 'Математика'
    )
    ''')

    cursor.execute("SELECT * FROM StudentGrades")

    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()


# Задание 2

# def main():
#
#     conn = sqlite3.connect('hospital.db')
#     conn.execute('PRAGMA foreign_keys=ON;')
#     cursor = conn.cursor()
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Departments (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Building INTEGER NOT NULL CHECK (Building BETWEEN 1 AND 5),
#         Financing REAL NOT NULL DEFAULT 0 CHECK (Financing >= 0),
#         Name TEXT NOT NULL UNIQUE CHECK (Name <> '')
#     )''')
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Diseases (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name TEXT NOT NULL UNIQUE CHECK (Name <> ''),
#         Severity INTEGER NOT NULL DEFAULT 1 CHECK (Severity >= 1)
#     )''')
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Doctors (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name TEXT NOT NULL CHECK (Name <> ''),
#         Phone CHAR(10),
#         Salary REAL NOT NULL CHECK (Salary > 0),
#         Surname TEXT NOT NULL CHECK (Surname <> '')
#     )''')
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Examinations (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         DayOfWeek INTEGER NOT NULL CHECK (DayOfWeek BETWEEN 1 AND 7),
#         StartTime TIME NOT NULL CHECK (StartTime >= '08:00' AND StartTime <= '18:00'),
#         EndTime TIME NOT NULL,
#         Name TEXT NOT NULL UNIQUE CHECK (Name <> ''),
#         CHECK (EndTime > StartTime)
#     )''')
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Wards (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Building INTEGER NOT NULL CHECK (Building BETWEEN 1 AND 5),
#         Floor INTEGER NOT NULL CHECK (Floor >= 1),
#         Name TEXT NOT NULL UNIQUE CHECK (Name <> '')
#     )''')
#
#     cursor.execute("INSERT OR IGNORE INTO Departments (Building, Financing, Name) VALUES (1, 50000, 'Терапия')")
#     cursor.execute(
#         "INSERT OR IGNORE INTO Doctors (Name, Surname, Salary, Phone) VALUES ('Григорий', 'Хаус', 15000, '0991234567')")
#     cursor.execute("INSERT OR IGNORE INTO Diseases (Name, Severity) VALUES ('Грипп', 2)")
#     cursor.execute("INSERT OR IGNORE INTO Wards (Building, Floor, Name) VALUES (1, 2, 'Палата №6')")
#     cursor.execute(
#         "INSERT OR IGNORE INTO Examinations (DayOfWeek, StartTime, EndTime, Name) VALUES (1, '09:00', '10:00', 'Рентген')")
#
#     conn.commit()
#
#     print("ОТДЕЛЕНИЯ")
#     cursor.execute("SELECT * FROM Departments")
#     for row in cursor.fetchall():
#         print(row)
#
#     print("\nВРАЧИ")
#     cursor.execute("SELECT * FROM Doctors")
#     for row in cursor.fetchall():
#         print(row)
#
#     print("\nЗАБОЛЕВАНИЯ")
#     cursor.execute("SELECT * FROM Diseases")
#     for row in cursor.fetchall():
#         print(row)
#
#     print("\nПАЛАТЫ")
#     cursor.execute("SELECT * FROM Wards")
#     for row in cursor.fetchall():
#         print(row)
#
#     print("\nОБСЛЕДОВАНИЯ")
#     cursor.execute("SELECT * FROM Examinations")
#     for row in cursor.fetchall():
#         print(row)
#
#     conn.close()
#
#
# if __name__ == "__main__":
#     main()