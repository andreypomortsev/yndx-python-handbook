import os
import signal
from io import StringIO
from types import FrameType
from typing import Callable, Tuple, Any, Union

import psutil
from pytest import FixtureRequest


class MemoryLimitExceeded(Exception):
    pass


class TimeLimitExceeded(Exception):
    pass


def memory_limit(limit_mb: int):
    """
    Декоратор для ограничения использования памяти в функции.

    Аргументы:
        limit_mb (int): Максимально допустимое использование памяти
            в мегабайтах.

    Исключения:
        MemoryLimitExceeded: Исключение, если использование памяти
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

    Аргументы:
        limit_seconds (int): Максимально допустимое время выполнения
            в секундах.

    Исключения:
        TimeLimitExceeded: Исключение, если время выполнения превышает \
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


def generate_error_msg(
    expected_output: str, printed_output: Union[str, set, tuple]
) -> str:
    """
    Формирует сообщение с напечатанными данными и ожидаемыми.

    Аргументы:
        printed_output (str): Ответ выданные модулем.
        expected_output (Union[str, set, tuple]): Ожидаемые данные вывода,
            могут быть: списком, множеством или кортежем.

    Возвращает:
        str: Сообщение с напечатанными данными и ожидаемыми.
    """
    return (
        f"\nExpected output:\n{expected_output}\n\n"
        f"Printed output:\n{printed_output}"
    )


def compare_output(
    printed_output: str, expected_output: Union[str, set, tuple, list]
) -> None:
    """
    Сравнивает напечатанный вывод с ожидаемым выводом.

    Аргументы:
        printed_output (str): Ответ выданные модулем.
        expected_output (Union[str, set, tuple]): Ожидаемые данные вывода,
            могут быть: строкой, списком, множеством или кортежем.
    Исключения:
        AssertionError: Если фактический вывод не совпадает с ожидаемым.
    """
    instance_type = type(expected_output)
    error_msg = generate_error_msg(printed_output, expected_output)

    if instance_type is set:
        assert printed_output in expected_output, error_msg
    # Передаются тесты в которых нужно оценить результат печати set
    # Так как множества неупорядочные приходится преобразовывать в set
    # Для сравнения двух множеств
    elif instance_type in {tuple, list}:
        if instance_type is tuple:  # Когда set распечатан в одну строку
            printed_output = set(printed_output)
            expected_output = set(expected_output[0])
        else:  # Когда set распечатан в несколько строк
            printed_output = set(printed_output.split("\n"))
            expected_output = set(expected_output[0].split("\n"))

        error_msg = generate_error_msg(printed_output, expected_output)

        # Сравниваем преобразованные в множества строки
        assert printed_output == expected_output, error_msg

    elif instance_type is str:
        assert printed_output == expected_output, error_msg


def assert_equal(
    wrapped_module: Callable[..., None],
    monkeypatch: Any,
    mock_input_text: str,
    expected_output: Union[str, set, tuple, list],
) -> None:
    """
    Запускает тест с заданным вводом и проверяет вывод.

    Аргументы:
        wrapped_module (Callable[..., None]): Модуль или функция,
            которые будут протестированы.
        monkeypatch (Any): Фикстура pytest, используемая для замены
            ввода и вывода
        mock_input_text (str): Входной текст для имитации ввода пользователя.
        expected_output (Union[str, set, tuple, list]): Ожидаемые данные вывода
    """
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    compare_output(printed_output, expected_output)


def get_tested_file_details(request: FixtureRequest) -> Tuple[str, str]:
    """
    Функция для получения пути к тестируемому файлу и его имени.

    Аргументы:
        request (FixtureRequest): Объект запроса pytest, содержащий информацию
            о текущем тесте.

    Возвращает:
        Tuple[str, str]: Кортеж, содержащий путь к тестируемому файлу и его имя
                без расширения.
    """
    # Получаем имя файла текущего модуля теста
    file_name = os.path.basename(request.module.__file__)

    # Получаем путь к директории, в которой находится текущий модуль теста
    dir_name = os.path.dirname(request.module.__file__)

    # Абсолюный путь в корневой каталог
    abs_code_dir = os.path.abspath(os.path.join(dir_name, "..", ".."))

    # Название папки с тестируемым кодом
    file_dir = os.path.basename(dir_name)

    # Получаем имя тестируемого файла "test_21_a.py" -> "a.py"
    tested_file_name = file_name.split("test_")[-1]

    # Путь к тестируемому файлу для обертывания в функцию
    path_to_test_file = os.path.join(
        abs_code_dir, "solutions", file_dir, tested_file_name
    )

    # Получаем букву тестируемого файла "a.py" -> ["a", ""]
    tested_file_name = tested_file_name.split(".py")[0]
    return path_to_test_file, tested_file_name
