import importlib
import os
import sys
from types import ModuleType
from typing import Generator, Tuple

import pytest
from _pytest.main import Session

from .utils import memory_limit, time_limit, get_tested_file_details

# Добавить родительский каталог в системный путь
# Это позволяет импортировать модули из родительского каталога
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="module")
def wrap_answer() -> Generator:
    def wrapper(file_path: str, file_name: str) -> None:
        """
        Считывает решение из файла и оборачивает его в main функцию
        для получения информации о покрытии тестов во время тестирования.

        Args:
            file_path (str): путь к файлу с решением.
            file_name (str): имя файла с решением.
        Returns:
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
    request, wrap_answer
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
    request -- объект, предоставляющий информацию о тестовом запросе.
    wrap_answer -- функция, которая оборачивает файл в функцию main и
    возвращает путь к обернутому файлу.

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


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session: Session):
    """
    Pytest hook, который запускается после завершения тестовой сессии.

    Этот хук удаляет все временные файлы, созданные во время тестирования.

    :param session: Текущая тестовая сессия Pytest.
    """
    # Удаляем все временные файлы
    if hasattr(session.config, "wrapped_file_paths"):
        for path_to_the_wrapped_file in session.config.wrapped_file_paths:
            if os.path.exists(path_to_the_wrapped_file):
                os.remove(path_to_the_wrapped_file)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    """
    Pytest hook для применения ограничений по памяти и времени к тестам.

    :param item: Тестовый элемент, к которому применяются ограничения.
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
