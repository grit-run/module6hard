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


    def _is_valid_sides(self):
        if len(self._sides) != self.sides_count:
            return False
        for side in self._sides:
            if side <= 0:
                return False
        return True

    def get_sides(self):
        return self._sides

    def set_sides(self, *sides):
        if self._is_valid_sides():
            self._sides = sides
        else:
            self._sides = [sides[0]] * self.sides_count

    #        print(self._sides)

    def __len(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__()
        self.set_color(color)
        self.set_sides(radius)

    def get_volume(self):
        return 2 * 3.14 * self._sides[0]

    def __len(self):
        return 2 * 3.14 * self._sides[0]


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__()
        self.set_color(color[0], color[1], color[2])
        self.set_sides(side1, side2, side3)

    def get_volume(self):
        return self._sides[0] * self._sides[1] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        super().__init__()
        self.set_color(color[0], color[1], color[2])
        self.set_sides(edge)

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 12)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())
#
## Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
#circle1.set_sides(15)  # Изменится
#print(cube1.get_sides())
#print(circle1.get_sides())
#
## Проверка периметра (круга), это и есть длина:
#print(len(circle1))
#
## Проверка объёма (куба):
#print(cube1.get_volume())
