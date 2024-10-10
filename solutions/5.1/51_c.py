class RedButton:
    def __init__(self) -> None:
        self.counter = 0

    def click(self) -> None:
        print("Тревога!")
        self.counter += 1

    def count(self) -> int:
        return self.counter
