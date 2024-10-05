class Point:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    def move(self, x: float | int, y: float | int) -> None:
        self.x += x
        self.y += y

    def length(self, other: "Point") -> float | int:
        distance_squared = (other.x - self.x) ** 2 + (other.y - self.y) ** 2
        return round(distance_squared**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *coordinates) -> None:
        if not coordinates:
            x, y = 0, 0
        elif isinstance(coordinates[0], tuple):
            x, y = coordinates[0]
        else:
            x, y = coordinates
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"
