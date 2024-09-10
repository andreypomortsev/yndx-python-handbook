import os
import signal
import tracemalloc
from io import StringIO
from types import FrameType, ModuleType
from typing import Any, Callable, List, Set, Tuple, Union

from _pytest.fixtures import SubRequest
from pytest import FixtureRequest

from .errors import MemoryLimitExceeded, TimeLimitExceeded


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
            tracemalloc.start()
            snapshot_before = tracemalloc.take_snapshot()

            result = func(*args, **kwargs)

            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            snapshot_before_stats = snapshot_before.statistics("lineno")
            memory_at_snapshot = sum(
                stat.size for stat in snapshot_before_stats
            )
            mem_usage = (peak - memory_at_snapshot) // (1024 * 1024)

            if mem_usage > limit_mb:
                msg = f"Использовано: {mem_usage: .2f} MB, лимит {limit_mb} MB"
                raise MemoryLimitExceeded(msg)

            return result

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
        def handler(signum: Union[int, float], frame: FrameType) -> None:
            msg = f"Тест занял больше лимита в {limit_seconds} сек."
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
    printed_output: str,
    expected_output: Union[Set[str], Tuple[str], List[str]],
) -> str:
    """
    Формирует сообщение с напечатанными данными и ожидаемыми.

    Аргументы:
        printed_output (str): Ответ выданные модулем.
        expected_output (Union[Set[str], Tuple[str], List[str]],): Ожидаемые
            данные вывода, могут быть: стрококй, списком, set или кортежем.

    Возвращает:
        str: Сообщение с напечатанными данными и ожидаемыми.
    """
    return (
        f"\nExpected output:\n{expected_output}\n\n"
        f"Printed output:\n{printed_output}"
    )


def compare_output(
    printed_output: str,
    expected_output: Union[Set[str], Tuple[str], List[str]],
) -> None:
    """
    Сравнивает напечатанный вывод с ожидаемым выводом.

    Аргументы:
        printed_output (str): Ответ выданные модулем.
        expected_output (Union[Set[str], Tuple[str], List[str]],): Ожидаемые
            данные вывода, могут быть: строкой, списком, set или кортежем.
    Исключения:
        AssertionError: Если фактический вывод не совпадает с ожидаемым.
    """
    if isinstance(expected_output, set):
        error_msg = generate_error_msg(printed_output, expected_output)
        assert printed_output in expected_output, error_msg
        return

    # Передаются тесты в которых нужно оценить результат печати set
    # Так как множества неупорядочные приходится преобразовывать в set
    # Для сравнения двух множеств
    if isinstance(expected_output, tuple):
        # Когда set распечатан в одну строку
        printed_output = set(printed_output)
        expected_output = set(expected_output[0])

    if isinstance(expected_output, list):
        # Когда set распечатан в несколько строк
        printed_output = set(printed_output.split("\n"))
        expected_output = set(expected_output[0].split("\n"))

    error_msg = generate_error_msg(printed_output, expected_output)
    assert printed_output == expected_output, error_msg


def assert_equal(
    wrapped_module: ModuleType,
    monkeypatch: Any,
    mock_input_text: Union[str, None],
    expected_output: Union[str, set, tuple, list],
) -> None:
    """
    Запускает тест с заданным вводом и проверяет вывод.

    Аргументы:
        wrapped_module (ModuleType): Модуль или функция,
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
    abs_code_dir = os.path.join(dir_name, "..", "..")

    # Название папки с тестируемым кодом
    file_dir = os.path.basename(dir_name)

    # Получаем имя тестируемого файла "test_21_a.py" -> "21_a.py"
    tested_file_name = file_name.split("test_")[-1]

    # Путь к тестируемому файлу для обертывания в функцию
    path_to_test_file = os.path.join(
        abs_code_dir, "solutions", file_dir, tested_file_name
    )

    # Получаем букву тестируемого файла "21_a.py" -> ["21_a", ""]
    tested_file_name = tested_file_name.split(".py")[0]

    return path_to_test_file, tested_file_name


def add_file_to_cleanup(
    request: SubRequest, path_to_the_temp_file: str
) -> None:
    # Добавляем пути временных файлов
    try:
        request.config.temp_file_paths.append(path_to_the_temp_file)
    except AttributeError:
        request.config.temp_file_paths = []
        request.config.temp_file_paths.append(path_to_the_temp_file)
