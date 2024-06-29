class Figure:
    sides_count = 0

    def __init__(self):
        self._sides = []
        self._color = (0, 0, 0)
        self.filled = False

    def get_color(self):
        return self._color

    def _is_valid_color(self, new_color):
        if isinstance(new_color, tuple) and len(new_color) == 3:
            if 255 >= new_color[0] >= 0 and 255 >= new_color[1] >= 0 and 255 >= new_color[2] >= 0:
                return True

    def set_color(self, *color):
        if self._is_valid_color(color):
            self._color = color

    def _is_valid_sides(self, new_sides):
        if isinstance(new_sides, tuple) and len(new_sides) == 1:
            return True

    def set_sides(self, *sides):
        if self._is_valid_sides(sides):
            self._sides = [sides[0]] * self.sides_count

    def get_sides(self):
        return self._sides

    def __len(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__()
        self._radius = side/(3.14*2)
        self.set_color(color)
        self.set_sides(side)

    def get_square(self):
        return 3.14 * self._radius ** 2

    def __len__(self):
        circum = self.get_sides()[0]
        return circum


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *edges):
        super().__init__()
        self.set_color(color)
        self.set_sides(edges)

    def get_volume(self):
        return self._sides[0] * self._sides[1] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        super().__init__()
        self.set_color(color[0], color[1], color[2])
        self.set_sides(edge)

    def set_sides(self, *sides):
        if len(sides) == 1:
            if self._is_valid_sides(sides):
                self._sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
#print(circle1.__dir__())
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())

