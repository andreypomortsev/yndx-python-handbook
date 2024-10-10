from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue: list[T] = []

    def push(self, item: T) -> None:
        self.queue.append(item)

    def pop(self) -> T:
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0
