import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        if self.filled:
            print('Фигура {} перекрашена в {} цвет'.format(self.__class__,self.__color))
        else:
            print('Фигура {} не перекрашена'.format(self.__class__))
        return self.__color

    def __is_valid_color(self,*col):
        for col in col:
            if isinstance(col, int) and 0 <= col <= 255:
                return True
            else:
                return False

    def set_color(self, *col):
        if self.__is_valid_color(*col):
            self.__color = col
            self.filled = True

    def __is_valid_sides(self, *side):
        for sid in side:
            if isinstance(sid, int) and sid > 0 and len(side) == self.sides_count:
                return True
            else:
                False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        print('Периметр фигуры {} равен {}'.format(self.__class__, sum(self.__sides)))
        return sum(self.__sides)

    def set_sides(self, *side):
        if self.__is_valid_sides(*side):
            self.__sides = list(side)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        self.__radius = self.get_sides()[0] / 2 / math.pi

    def get_radius(self):
        print('Радиус = ', end = '')
        return self.get_sides()[0] / 2 / math.pi

    def get_square(self):
        print("Площадь круга = ", end='')
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sid = self.get_sides()
        h_per = sum(sid)/2
        h = h_per
        for i in sid:
            h *= (h_per - i)
        sq = math.sqrt(h)
        print("Площадь треугольника = ", end='')
        return sq

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        volume = self.get_sides()[0]
        print("Объём куба = ", end='')
        return volume ** 3

tr = Triangle((10, 20, 30),3, 4, 5)
print(tr.get_square())
tr.set_color(200,20,40)
print(tr.get_color())
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
print(circle1.get_radius())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print(circle1.get_sides())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(circle1.get_radius())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())