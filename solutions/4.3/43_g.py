from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


def same_type(func: Callable[..., T]) -> Callable[..., str | T]:
    def wrapper(*args: Iterable[T], **kwargs) -> str | T:
        data_type = type(args[0])
        for data in args[1:]:
            if not isinstance(data, data_type):
                print("Обнаружены различные типы данных")
                return "Fail"
        else:
            return func(*args, **kwargs)

    return wrapper
