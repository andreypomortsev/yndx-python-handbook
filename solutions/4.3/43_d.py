from typing import Any, Callable


def answer(func: Callable[..., Any]) -> str:
    def wrapper(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper
