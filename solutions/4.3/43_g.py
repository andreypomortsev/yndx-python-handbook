from typing import Callable, Literal, TypeVar

T = TypeVar("T")


def same_type(func: Callable[..., T]) -> Callable[..., Literal["Fail"] | T]:
    def wrapper(*args: T, **kwargs: T) -> Literal["Fail"] | T:
        data_type = type(args[0])

        for data in args[1:]:
            if not isinstance(data, data_type):
                print("Обнаружены различные типы данных")
                return "Fail"

        return func(*args, **kwargs)

    return wrapper
