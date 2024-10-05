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
