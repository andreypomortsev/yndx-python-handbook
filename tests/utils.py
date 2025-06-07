import os
import tracemalloc
from io import StringIO
from types import ModuleType
from typing import Any, Callable, Optional, Tuple, TypeVar

from _pytest.fixtures import SubRequest
from func_timeout import FunctionTimedOut, func_timeout
from pytest import FixtureRequest, MonkeyPatch

from .errors import MemoryLimitExceeded, TimeLimitExceeded

T = TypeVar("T")


def memory_limit(
    limit_mb: int,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to limit the memory usage of a function.

    Arguments:
        limit_mb (int): Maximum allowed memory in megabytes.

    Raises:
        MemoryLimitExceeded: If execution memory exceeds the limit.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
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
                ML = f"Использовано: {mem_usage: .2f} MB, лимит {limit_mb} MB"
                raise MemoryLimitExceeded(ML)

            return result

        return wrapper

    return decorator


def time_limit(
    limit_seconds: int,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to limit the execution time of a function using multiprocessing.

    Arguments:
        limit_seconds (int): Maximum allowed time in seconds.

    Raises:
        TimeLimitExceeded: If execution time exceeds the limit.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func_timeout(
                    limit_seconds, func, args=args, kwargs=kwargs
                )
                return result
            except FunctionTimedOut:
                TL = f"Execution exceeded the limit of {limit_seconds} second."
                raise TimeLimitExceeded(TL)

        return wrapper

    return decorator


def get_mocked_print(
    wrapped_module: ModuleType,
    monkeypatch: MonkeyPatch,
    mock_input_text: Optional[str],
) -> str:
    """
    Executes the main function of the provided module with mocked input
    and output streams.

    Args:
        wrapped_module (ModuleType): The module whose main function
            will be executed.
        monkeypatch (MonkeyPatch): Pytest fixture for patching sys.stdin
            and sys.stdout.
        mock_input_text (Optional[str]): Text to simulate user input via stdin.

    Returns:
        str: The captured output produced by the module's main function.
    """
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    return printed_output


def get_tested_file_details(request: FixtureRequest) -> Tuple[str, str]:
    """
    Function to get the path to the file being tested and its name.

    Args:
        request (FixtureRequest): The pytest request object containing
            information about the current test.

    Returns:
        Tuple[str, str]: A tuple containing the path to the tested file
            and its name without the extension.
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


def count_function_calls(func: Callable[..., T]) -> Callable[..., T]:
    def wrapper(*args, **kwargs) -> T:
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper
