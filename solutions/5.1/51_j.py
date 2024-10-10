from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.stack: list[T] = []

    def push(self, item: T) -> None:
        self.stack.append(item)

    def pop(self) -> T:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0
