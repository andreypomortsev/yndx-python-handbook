class Point:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    def move(self, dx: float | int, dy: float | int) -> None:
        self.x += dx
        self.y += dy

    def length(self, other: "Point") -> float | int:
        distance_squared = (other.x - self.x) ** 2 + (other.y - self.y) ** 2
        return round(distance_squared**0.5, 2)
