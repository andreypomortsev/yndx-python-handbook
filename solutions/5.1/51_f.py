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

        x, y = self.get_pos()

        self.x_one = x
        self.y_one = y
        self.x_two = x + self.width
        self.y_two = y - self.height
