import signal
from types import FrameType
from typing import Callable, Any

import psutil


class MemoryLimitExceeded(Exception):
    pass


class TimeLimitExceeded(Exception):
    pass


def memory_limit(limit_mb: int):
    """
    Декоратор для ограничения использования памяти в функции.

    :param limit_mb: Максимально допустимое использование памяти в мегабайтах.
    :raises MemoryLimitExceeded: Исключение, если использование памяти \
        превышает указанный лимит.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args, **kwargs):
            process = psutil.Process()

            # Конвертируем в MB
            mem_usage = process.memory_info().rss / (1024 * 1024)

            if mem_usage > limit_mb:
                msg = f"Использовано: {mem_usage: .2f} MB, лимит {limit_mb} MB"
                raise MemoryLimitExceeded(msg)

            return func(*args, **kwargs)

        return wrapper

    return decorator


def time_limit(limit_seconds: int):
    """
    Декоратор для ограничения времени выполнения функции.

    :param limit_seconds: Максимально допустимое время выполнения в секундах.
    :raises TimeLimitExceeded: Исключение, если время выполнения превышает \
        указанный лимит.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def handler(signum: int | float, frame: FrameType) -> None:
            msg = f"Слишком долго: {limit_seconds} сек."
            raise TimeLimitExceeded(msg)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(limit_seconds)
            result = func(*args, **kwargs)
            signal.alarm(0)  # Выключаем alarm
            return result

        return wrapper

    return decorator


def get_elephants_text() -> str:
    """Данные для параграфа 2.1 тест G"""
    return """Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!"""
