import signal
from io import StringIO
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


def assert_equal(
    wrapped_module: Callable[..., None],
    monkeypatch: Any,
    mock_input_text: str,
    expected_output: str,
    is_set: bool = False,
) -> None:
    """
    Запускает тест с заданным вводом и проверяет вывод.

    :param wrapped_module: Модуль или функция, которые будут протестированы.
    :param monkeypatch: Фикстура pytest, используемая для замены ввода и вывода
    :param mock_input_text: Входной текст для имитации ввода пользователя.
    :param expected_output: Ожидаемый текст вывода для сравнения.
    :param equal: Флаг, определяющий способ сравнения. Если True,
        проверяется равенство фактического и ожидаемого вывода. Если False,
        проверяется, что фактический вывод содержится в ожидаемом.
    :raises AssertionError: Если фактический вывод не соответствует ожидаемому
        (или не содержится в ожидаемом, если equal=False).
    """
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    if is_set:
        assert printed_output in expected_output
    else:
        assert printed_output == expected_output
