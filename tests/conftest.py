import importlib
import os
import sys
from types import CodeType, ModuleType
from typing import Callable, Generator, Tuple

import pytest
from _pytest.main import Session
from pytest import FixtureRequest

from .utils import (
    compile_string,
    get_tested_file_details,
    memory_limit,
    time_limit,
)

# Добавить родительский каталог в системный путь
# Это позволяет импортировать модули из родительского каталога
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="module")
def wrap_answer() -> Generator[Callable[[str, str], str], None, None]:
    def wrapper(file_path: str, file_name: str) -> str:
        """
        Считывает решение из файла и оборачивает его в main функцию
        для получения информации о покрытии тестов во время тестирования.

        Аргументы:
            file_path (str): путь к файлу с решением.
            file_name (str): имя файла с решением.

        Возвращает:
            str: путь к обернутому файлу.
        """
        with open(file_path, encoding="UTF-8") as file_in:
            script = file_in.read()

        # Добавляем отступы для обертывания в функцию
        indented_script = script.replace("\n", "\n    ").rstrip(" ")

        # Обертываем считанный из файла код в функцию main
        wrapped_script = f"def main():\n    {indented_script}"

        # Определяем папку с тестами
        current_dir = os.path.dirname(__file__)

        # Создаем имя решения обернутого в функцию
        wrapped_file_name = f"wrapped_{file_name}.py"

        # Создаем путь в которуй запишем файл для оценки покрытия тестами
        path_to_save = os.path.join(current_dir, wrapped_file_name)

        with open(path_to_save, "w", encoding="UTF-8") as file_out:
            file_out.write(wrapped_script)

        # Возвращаем путь для его удаления файла после прохождения тестов
        return path_to_save

    return wrapper


@pytest.fixture(scope="module")
def setup_environment(
    request: FixtureRequest, wrap_answer: Callable[..., None]
) -> Generator[Tuple[ModuleType, str], None, None]:
    """
    Фикстура для настройки тестовой среды, которая оборачивает тестируемый
    файл в функцию main и динамически импортирует обернутый модуль.

    Эта фикстура выполняет следующие действия:
    1. Определяет имя текущего файла и каталог тестов.
    2. Определяет абсолютный путь к корневому каталогу исходного кода.
    3. Определяет папку с тестируемым кодом и имя тестируемого файла.
    4. Создает путь к тестируемому файлу и оборачивает его в функцию main
        с помощью `wrap_answer`, получая путь к обернутому файлу.
    5. Получает букву тестируемого файла для динамического импорта.
    6. Импортирует обернутый модуль после его создания.
    7. Добавляет путь к обернутому файлу в список временных файлов
        в конфигурации тестов для последующего удаления.

    Аргументы:
        request (FixtureRequest): объект, предоставляющий информацию
            о тестовом запросе.
        wrap_answer (Callable[..., None]): функция, которая оборачивает файл
            в функцию main и возвращает путь к обернутому файлу.

    Возвращает:
        tuple: Кортеж, содержащий импортированный модуль и путь
            к тестируемому файлу.
    """
    # Получаем путь к файлу с решением и его имя
    path_to_test_file, tested_file_name = get_tested_file_details(request)

    # Оборачиваем тестируемый файл в функцию main, получаем путь файла
    path_to_the_wrapped_file = wrap_answer(path_to_test_file, tested_file_name)

    # Динамически импортируем wrapped файл после создания
    wrapped_module_name = f"tests.wrapped_{tested_file_name}"
    wrapped_module = importlib.import_module(wrapped_module_name)

    # Добавляем пути временных файлов
    if not hasattr(request.config, "wrapped_file_paths"):
        request.config.wrapped_file_paths = []
    request.config.wrapped_file_paths.append(path_to_the_wrapped_file)

    yield wrapped_module, path_to_test_file


@pytest.fixture(scope="module")
def setup_environment_comprehension(
    request: FixtureRequest,
) -> Generator[CodeType, None, None]:
    """
    Фикстура для настройки тестовой среды, которая компилирует
    list/dict/set comprehension из файла в объект типа CodeType,
    готовый к исполнению.

    Эта фикстура выполняет следующие действия:
    1. Получает путь к файлу с решением -> `get_tested_file_details`.
    2. Компилирует код из файла в объект типа CodeType -> `compile_string`.
    3. Возвращает объект CodeType, который можно использовать в тестах.

    Аргументы:
        request (FixtureRequest): Объект, предоставляющий информацию
            о тестовом запросе.

    Возвращает:
        Generator[CodeType, None, None]: Генератор, который возвращает
            объект CodeType.
    """
    # Получаем путь к файлу с решением
    path_to_test_file, _ = get_tested_file_details(request)

    # Компилируем list/dict/set comprehension в готовый к исполнению код
    ready_to_eval = compile_string(path_to_test_file)

    yield ready_to_eval


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session: Session) -> None:
    """
    Pytest hook, который запускается после завершения тестовой сессии.

    Этот хук удаляет все временные файлы, созданные во время тестирования.

    Аргументы:
        session (Session): Текущая тестовая сессия Pytest.
    """
    # Удаляем все временные файлы
    if hasattr(session.config, "wrapped_file_paths"):
        for path_to_the_wrapped_file in session.config.wrapped_file_paths:
            if os.path.exists(path_to_the_wrapped_file):
                os.remove(path_to_the_wrapped_file)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item: pytest.Item) -> Generator[None, None, None]:
    """
    Pytest hook для применения ограничений по памяти и времени к тестам.

    Аргументы:
        item (pytest.Item): Тестовый элемент, к которому применяются
            ограничения.
    """
    memory_limit_marker = item.get_closest_marker("memory_limit")
    time_limit_marker = item.get_closest_marker("time_limit")

    if memory_limit_marker:
        limit_mb = memory_limit_marker.args[0]
        item.obj = memory_limit(limit_mb)(item.obj)

    if time_limit_marker:
        limit_seconds = time_limit_marker.args[0]
        item.obj = time_limit(limit_seconds)(item.obj)

    yield
