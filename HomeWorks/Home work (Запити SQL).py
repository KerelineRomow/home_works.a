import sqlite3


def main():
    conn = sqlite3.connect('students_grades.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS StudentGrades")

    cursor.execute('''
    CREATE TABLE StudentGrades (
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

    students = [
        ('Иванов Иван Иванович', 'Киев', 'Украина', '2005-05-15', 'ivanov@example.com', '+380991234567', 'П-11', 10.5, 'Физика', 'Математика'),
        ('Борис Петров', 'Одесса', 'Украина', '2006-03-12', 'boris@test.com', '+380777123456', 'П-11', 8.2, 'Химия', 'Биология'),
        ('Анна Сидорова', 'Киев', 'Украина', '2004-11-20', 'anna@example.com', '+380667778899', 'П-12', 11.9, 'Математика', 'Физика'),
        ('Джон Доу', 'Лондон', 'Англия', '2006-01-01', 'john@mail.com', '+4401234567', 'П-12', 9.5, 'История', 'География')
    ]

    cursor.executemany(
        '''INSERT INTO StudentGrades
        (full_name, city, country, birth_date, email, phone, group_name,
         avg_yearly_grade, min_grade_subject, max_grade_subject)
        VALUES (?,?,?,?,?,?,?,?,?,?)''',
        students
    )

    conn.commit()

    # Задание 1

    print("Задание 1")

    print("\n1. Вся информация:")
    cursor.execute("SELECT * FROM StudentGrades")
    for row in cursor:
        print(row)

    print("\n2. ФИО всех студентов:")
    cursor.execute("SELECT full_name FROM StudentGrades")
    for row in cursor:
        print(row[0])

    print("\n3. Все средние оценки:")
    cursor.execute("SELECT avg_yearly_grade FROM StudentGrades")
    for row in cursor:
        print(row[0])

    print("\n4. ФИО где средняя оценка больше указанной:")
    limit_grade = 9
    cursor.execute(
        "SELECT full_name FROM StudentGrades WHERE avg_yearly_grade > ?",
        (limit_grade,)
    )
    for row in cursor:
        print(row[0])

    print("\n5. Уникальные страны:")
    cursor.execute("SELECT DISTINCT country FROM StudentGrades")
    for row in cursor:
        print(row[0])

    print("\n6. Уникальные города:")
    cursor.execute("SELECT DISTINCT city FROM StudentGrades")
    for row in cursor:
        print(row[0])

    print("\n7. Уникальные группы:")
    cursor.execute("SELECT DISTINCT group_name FROM StudentGrades")
    for row in cursor:
        print(row[0])

    print("\n8. Предметы с минимальной средней оценкой:")
    cursor.execute("""
        SELECT DISTINCT min_grade_subject
        FROM StudentGrades
        WHERE avg_yearly_grade = (
            SELECT MIN(avg_yearly_grade) FROM StudentGrades
        )
    """)
    for row in cursor:
        print(row[0])

    # Задание 2

    print("\nЗадание 2")

    print("\n1. ФИО где оценка в диапазоне 8-11:")
    cursor.execute("""
        SELECT full_name
        FROM StudentGrades
        WHERE avg_yearly_grade BETWEEN 8 AND 11
    """)
    for row in cursor:
        print(row[0])

    print("\n2. Студенты которым 20 лет:")
    cursor.execute("""
        SELECT *
        FROM StudentGrades
        WHERE (strftime('%Y','now') - strftime('%Y', birth_date)) = 20
    """)
    for row in cursor:
        print(row)

    print("\n3. Студенты с возрастом в диапазоне 19-21:")
    cursor.execute("""
        SELECT *
        FROM StudentGrades
        WHERE (strftime('%Y','now') - strftime('%Y', birth_date))
              BETWEEN 19 AND 21
    """)
    for row in cursor:
        print(row)

    print("\n4. Студенты с именем Борис:")
    cursor.execute("""
        SELECT *
        FROM StudentGrades
        WHERE full_name LIKE '%Борис%'
    """)
    for row in cursor:
        print(row)

    print("\n5. Телефоны содержащие минимум три '7':")
    cursor.execute("""
        SELECT *
        FROM StudentGrades
        WHERE LENGTH(phone) - LENGTH(REPLACE(phone,'7','')) >= 3
    """)
    for row in cursor:
        print(row)

    print("\n6. Email на букву 'i':")
    cursor.execute("SELECT email FROM StudentGrades WHERE email LIKE 'i%'")
    for row in cursor:
        print(row[0])

    conn.close()


if __name__ == "__main__":
    main()