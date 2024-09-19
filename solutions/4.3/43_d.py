from typing import Callable, TypeVar

T = TypeVar("T")


def answer(func: Callable[..., T]) -> Callable[..., str]:
    def wrapper(*args, **kwargs) -> str:
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper
