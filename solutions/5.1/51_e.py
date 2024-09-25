class Rectangle:
    def __init__(
        self,
        point_one: tuple[float | int, float | int],
        point_two: tuple[float | int, float | int],
    ):
        self.x_one, self.y_one = point_one
        self.x_two, self.y_two = point_two
        self.height = abs(self.y_one - self.y_two)
        self.width = abs(self.x_one - self.x_two)

    def perimeter(self) -> float | int:
        calculated_perimeter = (self.height + self.width) * 2
        return round(calculated_perimeter, 2)

    def area(self) -> float | int:
        calculated_area = self.height * self.width
        return round(calculated_area, 2)
