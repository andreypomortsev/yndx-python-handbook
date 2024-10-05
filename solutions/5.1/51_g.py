class Rectangle:
    def __init__(self, point_one: tuple, point_two: tuple) -> None:
        self.x_one, self.y_one = point_one
        self.x_two, self.y_two = point_two

        self.height = abs(self.y_one - self.y_two)
        self.width = abs(self.x_one - self.x_two)

    def perimeter(self) -> float:
        calc_perimeter = (self.height + self.width) * 2

        return round(calc_perimeter, 2)

    def area(self) -> float:
        calc_area = self.height * self.width

        return round(calc_area, 2)

    def get_pos(self) -> tuple:
        x = min(self.x_one, self.x_two)
        y = max(self.y_one, self.y_two)

        return round(x, 2), round(y, 2)

    def get_size(self) -> tuple:
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx: float | int, dy: float | int) -> None:
        self.x_one += dx
        self.x_two += dx
        self.y_one += dy
        self.y_two += dy

    def resize(self, width: float | int, height: float | int) -> None:
        self.width = width
        self.height = height

    def turn(self) -> None:
        center_x, center_y = self._get_center()

        new_x_one = center_x - (self.y_one - center_y)
        new_y_one = center_y + self.x_one - center_x

        new_x_two = center_x - (self.y_two - center_y)
        new_y_two = center_y + self.x_two - center_x

        self.x_one, self.y_one = new_x_one, new_y_one
        self.x_two, self.y_two = new_x_two, new_y_two

        self.width, self.height = self.height, self.width

    def scale(self, factor: float | int) -> None:
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)

        center_x, center_y = self._get_center()

        self.x_one = (self.x_one - center_x) * factor + center_x
        self.y_one = (self.y_one - center_y) * factor + center_y

        self.x_two = (self.x_two - center_x) * factor + center_x
        self.y_two = (self.y_two - center_y) * factor + center_y

    def _get_center(self) -> tuple:
        center_x = (self.x_one + self.x_two) / 2
        center_y = (self.y_one + self.y_two) / 2

        return center_x, center_y
