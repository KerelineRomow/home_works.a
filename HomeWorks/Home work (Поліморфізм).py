# Задание 1

class Airplane:
    def __init__(self, plane_type, max_passengers, passengers):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.passengers = passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, value):
        self.passengers += value
        return self

    def __sub__(self, value):
        self.passengers -= value
        return self

    def __iadd__(self, value):
        self.passengers += value
        return self

    def __isub__(self, value):
        self.passengers -= value
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

# plane1 = Airplane("Boeing", 300, 100)
# plane2 = Airplane("Boeing", 200, 150)
#
# print(plane1 == plane2)
#
# plane1 + 10
# plane1 - 5
# plane1 += 20
# plane1 -= 10
#
# print(plane1 > plane2)
# print(plane1 < plane2)
# print(plane1 >= plane2)
# print(plane1 <= plane2)


# Задание 2

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

# flat1 = Flat(50, 70000)
# flat2 = Flat(60, 65000)
#
# print(flat1 == flat2)
# print(flat1 != flat2)
#
# print(flat1 > flat2)
# print(flat1 < flat2)
# print(flat1 >= flat2)
# print(flat1 <= flat2)


# Задание 3

class Shape:
    def Show(self):
        pass

    def Save(self, file):
        pass

    def Load(self, data):
        pass

class Square(Shape):
    def __init__(self, x=0, y=0, side=0):
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"Квадрат: x={self.x}, y={self.y}, сторона={self.side}")

    def Save(self, file):
        file.write(f"Square {self.x} {self.y} {self.side}\n")

    def Load(self, data):
        self.x, self.y, self.side = map(int, data)


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Прямоугольник: x={self.x}, y={self.y}, ширина={self.width}, высота={self.height}")

    def Save(self, file):
        file.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")

    def Load(self, data):
        self.x, self.y, self.width, self.height = map(int, data)


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=0):
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Круг: центр=({self.x}, {self.y}), радиус={self.radius}")

    def Save(self, file):
        file.write(f"Circle {self.x} {self.y} {self.radius}\n")

    def Load(self, data):
        self.x, self.y, self.radius = map(int, data)


class Ellipse(Shape):
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Эллипс: x={self.x}, y={self.y}, ширина={self.width}, высота={self.height}")

    def Save(self, file):
        file.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")

    def Load(self, data):
        self.x, self.y, self.width, self.height = map(int, data)



shapes = [
    Square(1, 1, 10),
    Rectangle(2, 2, 20, 10),
    Circle(5, 5, 7),
    Ellipse(0, 0, 15, 8)
]

with open("shapes.txt", "w") as file:
    for shape in shapes:
        shape.Save(file)

loaded_shapes = []

with open("shapes.txt", "r") as file:
    for line in file:
        parts = line.split()
        shape_type = parts[0]
        data = parts[1:]

        if shape_type == "Square":
            shape = Square()
        elif shape_type == "Rectangle":
            shape = Rectangle()
        elif shape_type == "Circle":
            shape = Circle()
        elif shape_type == "Ellipse":
            shape = Ellipse()

        shape.Load(data)
        loaded_shapes.append(shape)

for shape in loaded_shapes:
    shape.Show()